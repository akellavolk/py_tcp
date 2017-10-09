"""Socket's clientside"""
import socket
SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCK.connect(('127.0.0.1', 2222))
while True:
    MSG = raw_input()
    SOCK.send(MSG)
    if MSG == 'close':
        break
    RESPONSE = SOCK.recv(1024)
    print RESPONSE
SOCK.close()
