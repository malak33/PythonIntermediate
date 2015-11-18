"""

        13_json_rpc_server.py  -   This requires an install of json-rpc
                                first.  pip install json-rpc.

                                Run this first then run 14_json_rpc_client.py

"""
import requests
import json


url = "http://localhost:8005/jsonrpc"
headers = {'content-type': 'application/json'}

school = input('Enter school name to retrieve: ')

payload = {
    "method": 'get_location',
    "params": [school],
    "id": 0
}
response = requests.post(url, data=json.dumps(payload), headers=headers).json()

results = response['error'] if response['error'] else response['result']
print(results)
