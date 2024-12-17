# ECHO SERVER

import socket # network
import os # perform terminal operations
import threading # multiple instances

server_ip = "127.0.0.1"
server_port = 7000
server_address = (server_ip, server_port)

def reader(sock): # receives and displays message data; always running
    while True: # loop to receive messages more than once
        try:
            response = sock.recv(1024) # arbitrary number of bytes
            response = str(response, "UTF-8") # format the bytes data as a string
            print()
            print(response)
            print()
        except: # if client exits or server ends...
            print("Client Disconnected")
            os._exit(0)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # alias for network things
    sock.connect(server_address) # connect to the server
    print(f"Connected to server: {server_address}") # confirmation



    # sock.bind(server_address) # associate socket with server address; bind() expects a tuple
    # sock.listen() # you can specify how many active connections there can be at a time here



    # allows for multiple instances of this to run
    thread = threading.Thread(target=reader, args=(sock,)) # pass in the function and arguments (must be tuple, even though there is only one field) to thread into multiple instances
    thread.start() # run a new thread
    thread.join() # wait for the thread to be done before returning ~control to main()
    # supposedly can also print(thread), but we won't know at what point in the thread it is printing

    print("Send messages through the terminal ['q' to quit]: ") # prompt once
    while True: # loop to write messages more than once
        message = input() # store string input
        if message == "q":
            break
        message = bytes(message, "UTF-8") # convert the string to bytes ("data")
        sock.sendall(message) # send the data to the server (through the network, as bytes)

# falling out of this with block will close the socket

print("Client closed. Have a nice day.")