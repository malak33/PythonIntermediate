# the server
import socket

sock = socket.socket()

server = socket.gethostname()
port = 8501
backlogQueue = 3
sock.bind((server, port))                                   # bind to a local address
sock.listen(backlogQueue)                                   # num connections to allow (queue) before refusing
print('Server running on port {num}'.format(num=port))
while True:
    client_conn, client_address = sock.accept()             # wait for an incoming connection, returns client connection and client address
    print('Client connected: ', client_address)
    client_conn.send(b'Welcome to my server!')
    client_conn.close()