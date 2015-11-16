"""
    Uses sockets to retrieve raw data from google maps.  Last 5 lines
    parse the raw response, extract the HTTP body from the HTTP response,
    parse it, and display the name of the first result.
"""
import json
import socket
from urllib.parse import quote_plus
from io import StringIO

request_str = """\
GET /maps/api/geocode/json?address={0}&sensor=false HTTP/1.1\r\n\
Host: maps.google.com:80\r\n\
User-Agent: 12_socket_geocode.py\r\n\
Connection: close\r\n\
\r\n\
"""

address = 'Walt Disney World, Lake Buena Vista, FL'

sock = socket.socket()
sock.connect(('maps.google.com', 80))

request = request_str.format(quote_plus(address))
sock.sendall(request.encode('ascii'))
response = []
while True:
    data = sock.recv(4096)
    if not data:
        break
    response.append(data)

response_str = b''.join(response).decode()
print(response_str)

response_lines = StringIO(response_str).readlines()
for count, line in enumerate(response_lines):
    if len(line.strip()) == 0:
        json_response = response_lines[count+1:]
        break

geo_object = json.loads(''.join(json_response))
print(geo_object['results'][0]['address_components'][0]['long_name'])