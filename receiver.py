#!/usr/bin/python

import socket
from scapy.all import *
"""
ip = sys.argv[1]
port = sys.argv[2]
"""
ip = "127.0.0.1"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((ip, int(port)))
s.listen(1)

while True :
    conn, addr = s.accept()
    print('Connection address:', addr)
    data = conn.recv(1024) #
