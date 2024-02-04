# udp_client.py

# code from page 11 of the book for building a UDP client

import socket

target_host = "127.0.0.1"
target_port = 9997

# create the socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data
client.send(b"AAABBBCCC", (target_host, target_port))

# recevie data
data, addr = client.recvfrom(4096)

# print
print(data.decode())
client.close()