# ECHO SERVER

import socket # network
import threading # multiple instances

server_ip = "127.0.0.1"
server_port = 7000
server_address = (server_ip, server_port)

clients = {} # Key = Connection; Value = Address
clients_lock = threading.Lock() # prevents multiple users from using the same client key at the same time
    # only ONE user will edit the client keys at a time until whatever block this is in is finished,
    # ensuring all generated/saved keys are unique

def broadcast(message, connection): # sends messages to client connections
    with clients_lock: # below can only be changed by one user at a time
        for client in clients.keys(): # go through all clients
            if client != connection: # if this client iteration is not the sender...
                client.sendall(message) # send the message to this client

# MULTI THREAD -- can host multiple clients
def client_connect(connection, address):
    with clients_lock:
        clients[connection] = address # add to the dictionary
    
    while True: # continuously check for message data to display
        # now that we're connected, let's read some information from the user
        data = connection.recv(1024) # (arbitrary number of bytes)
        if len(data) == 0: # if there is no message data...
            break # ...do not continue
        print(f"Received: {data}")

        # connection.sendall(data) # report/send all data again; goes to all clients

# Modify the server to obtain information from a local file in response to a request from the client.
# Would be something like:
        # if data == "soliloquy":
        #     while not EOF:
        #         printline(hamlets_soliloquy.txt)
        # else:
        broadcast(data, connection) # args take in message data and sender

    print(f"Client Disconnected: {address}") # report out of the loop
    with clients_lock:
        del clients[connection]
        # connection.close() # needed? there seems to be something that causes an error ("forcibly closed").
    

# MAIN THREAD -- only runs one instance
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(server_address) # associate socket with server address; bind() expects a tuple
    sock.listen() # you can specify how many active connections there can be at a time here
    print(f"Server started: {server_address}")

    while True:
        connection, address = sock.accept() # waits here until someone connects; stores connection and address results
        print(f"Client connected: {address}")
        client_thread = threading.Thread(target=client_connect,
                                         args = (connection, address))
        client_thread.start()

# falling out of this with block will close the socket

print("Server closed. See you later!")