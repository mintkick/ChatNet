# ECHO SERVER

import socket # network
import threading # multiple instances

server_ip = "127.0.0.1"
server_port = 7000
server_address = (server_ip, server_port)

clients = {} # Key = Connection; Value = Address

# wins = {} # Key = Connection; Value = Count

def broadcast(message, connection): # sends messages to client connections


    for client in clients.keys(): # go through all clients
        if client != connection: # if this client iteration is not the sender...
            client.sendall(message) # send the message to this client

player_move = {} # Key = connection; Value = move
# Should it be address instead?

# MULTI THREAD -- can host multiple clients
def client_connect(connection, address):
    clients[connection] = address # add to the dictionary
#    wins[connection] = 0
    
    while True: # continuously check for message data to display
        # now that we're connected, let's read some information from the user

        # assign a value (client's move) to a key (client's connection)
        # Should it be address instead?
        player_move[connection] = connection.recv(1024) # assign the move (value) to the player connection (key)
                                                        # (arbitrary number of bytes)
        if player_move[connection] is None: # if there is no message data...
        # if len(player_move.values) < 2: # == 0
            break # ...do not continue
        # print(f"Received move: {player_move.keys()}: {player_move.values()}")
        print(f"Received move: {connection}: {player_move[connection]}")
        # when running in error, shows:
        # Received move: <socket.socket fd=400, family=2, type=1, proto=0, laddr=('127.0.0.1', 7000), raddr=('127.0.0.1', 62911)>: b''

        # compare(player_move, )

        # connection.sendall(data) # report/send all data again; goes to all clients

        # once server receives data from all clients, evaluate and broadcast results
        if player_move.values == 2: # once we have received 2 or more moves...
            broadcast(player_move, connection) # args take in message data and sender

        # Hmm... Maybe receive the first player's move and then do a wait message while we wait for a second one?

    print(f"Client Disconnected: {address}") # report out of the loop
    del clients[connection]
#    del wins[connection]
    connection.close() # needed?


def compare(address, you, opponent):
    # convert the chars to uppercase
    you = str.upper(you)
    opponent = str.upper(opponent)

    # uses char int values to compare moves
    # if the difference is comparable to any of these combinations...
    if (you - opponent) == ('S' - 'P') or ('P' - 'R') or ('R' - 'S'):
        win += 1
    elif you == opponent:
        address.draw += 1
    else:
        address.lose =+ 1
    

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

print("Server closed. Have a nice day.")











# we can't reach into another cubicle and do another employee's work from your own.
# so instead, we send across a message to our coworker to do the task on HIS side.