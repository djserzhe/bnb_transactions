import requests
import json
import time
import os

def current_block_number(url: str) -> int:
    try:
        headers = {'Content-Type': 'application/json'}
        body = {
            'jsonrpc': '2.0',
            'method': 'eth_blockNumber',
            'params': [],
            'id': 'getblock.io'
        }

        res = requests.post(url, headers=headers, json=body)
        data = json.loads(res.text)
        current_block = int(data['result'],16)
        return current_block
    except Exception as e:
        print(f'Error while getting last block number: {e}')
        return -1
    
def transactions_of_block(url: str, block: int):
    try:
        headers = {'Content-Type': 'application/json'}
        body = {
            'jsonrpc': '2.0',
            'method': 'eth_getBlockByNumber',
            'params': [hex(block), True],
            'id': 'getblock.io'
        }

        res = requests.post(url, headers=headers, json=body)
        data = json.loads(res.text)

        for tr in data['result']['transactions']:           
            if int(tr['value'], 16) == 0:
                continue
            print(f"{tr['hash']} {tr['from']} {tr['to']} {int(tr['value'], 16) / 10**18}")
    except Exception as e:
        print(f'Error while getting transactions of block {block}: {e}')

def main():
    url = os.environ['BNB_TRANS_URL']
    request_interval = int(os.environ['BNB_TRANS_REQUEST_INTERVAL'])

    current_block = current_block_number(url)
    if current_block == -1:
        return
    previous_block = current_block

    while True:
        for block in range(previous_block, current_block + 1):
            transactions_of_block(url, block)
        time.sleep(request_interval)
        previous_block = current_block + 1
        current_block = current_block_number(url)
        if current_block == -1:
            return

if __name__ == "__main__":
    main()