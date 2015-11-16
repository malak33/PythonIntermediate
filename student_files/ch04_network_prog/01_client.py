import socket

sock = socket.socket()
server = socket.gethostname()           # you would have to know this

print('Connecting to {server}...'.format(server=server))
port = 8501


# version 1
sock.connect((server, port))            # IP sockets use (host, port) to connect
byte_data = sock.recv(1024)             # blocks until data received
print(byte_data.decode())
sock.close()


# you may use 'with' with sockets as of Python 3.2:
# version 2
with socket.socket() as sock:
    sock.connect((server,port))
    byte_data = sock.recv(1024)
    print(byte_data.decode())



# if you don't have Python 3.2+, you can use the closing wrapper from contextlib
# to assist in using the 'with' statement:
# version 3
from contextlib import closing
with closing(socket.socket()) as sock:
    sock.connect((server,port))
    byte_data = sock.recv(1024)
    print(byte_data.decode())



# version 4 uses the contextmanager decorator
from contextlib import contextmanager

@contextmanager
def socketcontextmgr():
    sock = socket.socket()
    yield sock
    sock.close()

with socketcontextmgr() as sock:
    sock.connect((server,port))
    byte_data = sock.recv(1024)
    print(byte_data.decode())


