#!/usr/bin/env python
#        _   _
#      _(_)_(_)_
#     |___@_@___|
#         | |
#        /(.)\
#       /_|||_\
#


import socket

def request_handler(req):
    buf = req.recv(1024)
    print buf
    req.send("HTTP/1.1 200 OK\r\n\r\n")
    req.send("<h2>Hello Ryan<h2><li>python</li><li>django</li>")

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',8008))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        request_handler(connection)
        connection.close()

if __name__ == '__main__':
    main()
