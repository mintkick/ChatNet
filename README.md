## Overview

**Project Title**: Python Chat Network

**Project Description**:
Chat with users in a Python terminal connected to a server. The server is likewise run on a terminal, and all of the connections are shared on a local network. While fun, it's probably not practical to use; this is simply to demonstrate that I am learning how to use network capabilities.

**Project Goals**:

- The server listens for connections on an IP address/localhost and a selected port number
- The client connects to an already waiting server
- The client sends at least one type of request message to the server
- The server processes the request and sends a response back to a client
- The server can handle a client disconnecting, allowing another client to connect

**Stretch Goal**:
Provide support for two or more clients (or peers) to connect to the server at the same time.
OR
Modify the server or the peer to obtain information from a local file or database in response to a request from the client or another peer.

## Instructions for Build and Use

Steps to build and/or run the software:

1. In one terminal, run `python server.py`
2. In any additional terminals, run `python client.py`

Instructions for using the software:

1. Any client can then type and send messages to all other clients on the network.
2. To leave, send `q` in the terminal.
3. To end the server, since it is configured to continuously run listening for client connections and messages, its terminal must be killed/trashed.

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

- VSCode
- Python 3 (I was using v3.12.6)
- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

## Useful Websites to Learn More

I found these websites useful in developing this software:

- [VSCode Server](https://code.visualstudio.com/docs/remote/vscode-server)
- [(Video) Python Network Programming #2: Server-Client Connection](https://www.youtube.com/watch?v=sN0r6Jz9dvI)
- [(Video) Python Socket Programming Tutorial](https://www.youtube.com/watch?v=3QiPPX-KeSc)
- [(Video) Creating a Simple Socket Server and Client in Python](https://www.youtube.com/watch?v=sUzM-vIC-s4)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

- [ ] Rock Paper Scissors against server computer
- [ ] Rock Paper Scissors against client opponent
- [ ] Track number of wins for each player
- [ ] Add a GUI
