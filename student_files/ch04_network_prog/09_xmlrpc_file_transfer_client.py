import xmlrpc.client

working_dir = 'downloads'
filename = 'harry.jpg'
host = 'localhost'
port = 8053

proxy = xmlrpc.client.ServerProxy('http://localhost:8053/')
with open('{path}/{filename}'.format(path=working_dir, filename=filename), 'wb') as f:
    image_data = proxy.get_file().data
    f.write(image_data)
