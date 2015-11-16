"""
    05_sendfile.py  -   This file serves as both a client and a server for
                        uploading a file.

                        When run with no arguments, the server will begin.
                        when run with one argument, the argument will become the
                        name of the file to upload (example: 05_sendfile.py test_upload_file.txt)

                        By default, the file will be uploaded into the uploads directory.

                        Note: to use PyCharm to run this both ways:
                        1. First right-click this file to run it as a server.
                        2. Then select Run > Edit Configurations...
                        3. In the configurations, click the third button (to the right
                           of the '-' (minus sign) to copy the configuration.  Give it
                           a name of client and a script parameter of _________ where
                           ___________ is the name of the file to upload.  Now run the
                           client.
"""
import socket
import sys
import time


class SendFile:
    def __init__(self, remote=None, port=80):
        self.remote = remote
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def upload(self, file_name):
        """
            Called by the client to send the file.
            :param file_name: a file to be sent by the client
            :return: None
        """
        self.sock.connect((self.remote, self.port))
        self.sock.send('{fn:1024}'.format(fn=file_name).encode('utf8'))     # we pad the filename to 1024 bytes because SOCK_STREAM (TCP) is streaming content and the packets will merge.  Therefore we need to know the length of the incoming field

        with open(file_name, 'rb') as f:
            while True:
                data = f.read()
                if not data:
                    break
                self.sock.sendall(data)

        self.sock.send(b'EOFX')

    def receive(self, client_conn):
        """
            Called by the server to receive a file
            :param client_conn: is a socket object returned from serversock.accept()
            :return: None
        """
        file_name = client_conn.recv(1024).decode('utf8').strip()

        print('Receiving File from client: {fn}'.format(fn=file_name))

        file_data = client_conn.recv(1024)

        if file_data != 'EOFX':
            with open('uploads/{fn}'.format(fn=file_name), 'wb') as f:
                while file_data:
                    if file_data.endswith(b'EOFX'):
                        f.write(file_data[:-4])
                        print('{fn} uploaded'.format(fn=file_name))
                        break
                    else:
                        f.write(file_data)
                        file_data = client_conn.recv(1024)


def create_server():
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servername = socket.gethostname()
    port = 8501
    backlog_queue = 3
    serversock.bind((servername, port))                         # bind to a local address
    serversock.listen(backlog_queue)                            # num connections to allow (queue) before refusing

    print('{server} running on port {num}'.format(server=servername, num=port))

    while True:
        client_conn = None
        client_conn, client_address = serversock.accept()       # wait for an incoming connection, returns client connection and client address
        print('Client connected: ', client_address)
        time.sleep(5)
        SendFile().receive(client_conn)
        client_conn.close()


def create_client(file_name):
    SendFile(socket.gethostname(), 8501).upload(file_name)


# if any argument is provided on the command-line, this program becomes a client
# otherwise this will act like a server.  The argument should be the name of the file to transfer
if len(sys.argv) >= 2:
    file_name = sys.argv[1]
    create_client(file_name)
else:
    create_server()
