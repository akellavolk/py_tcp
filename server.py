"""Sockets serverside"""
import socket
import threading

def response(connection, address):
    """Generates response"""
    while True:
        chunk = connection.recv(1024)
        if not chunk or chunk == 'close':
            print 'Connection closed ', address
            break
        connection.send(chunk.upper())
    connection.close()

SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCK.bind(('localhost', 2222))
SOCK.listen(10)
while True:
    (CONN, ADDR) = SOCK.accept()
    print 'Connection from ', ADDR
    THREAD = threading.Thread(target=response, args=(CONN, ADDR))
    THREAD.start()
