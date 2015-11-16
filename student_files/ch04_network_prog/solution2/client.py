import os
from xmlrpc.client import ServerProxy, Binary

from ch04_network_prog.solution2.globals import host, port


def send_file(filename, is_public=False):
    results = False
    proxy = ServerProxy('http://{host}:{port}'.format(host=host, port=port), allow_none=True)
    with open(filename, 'rb') as f:
        path, fn = os.path.split(filename)
        print('Sending {fn}'.format(fn=fn))
        data = f.read()
        results = proxy.upload(fn, Binary(data), is_public)

    return results


def list_public():
    proxy = ServerProxy('http://{host}:{port}'.format(host=host, port=port), allow_none=True)
    return proxy.list_public()


def remove(filename):
    proxy = ServerProxy('http://{host}:{port}'.format(host=host, port=port), allow_none=True)
    return proxy.remove(filename)


if __name__ == '__main__':
    print('Run server.py then run task4_1_starter.py next')
