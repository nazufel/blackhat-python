# tcp_client.py

# code from page 10 of the book on building a tcp client

import socket

target_host = "localhost"
target_port = 9998

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.sendto(b"AAABBBCCC", (target_host, target_port))

#receive some data
response = client.recv(4096)

# print the response and close the connection
print(response.decode())
client.close()