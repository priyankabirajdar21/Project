#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '0.0.0.0'
port = 12650                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
string = c.recv(1024).decode()
c.send(bytes(str(len(string)),'utf-8'))
c.close()                # Close the connection
