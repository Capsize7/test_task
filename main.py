import base64
import json
from pprint import pprint

import requests

API_URL = 'https://akash-rest.publicnode.com/blocks/'


def get_block_data(block_height: int | str) -> None:
    block_path = API_URL + str(block_height)
    block_data = requests.get(block_path)
    converted_block_data = json.loads(block_data.content)
    try:
        data_txs = converted_block_data['block']['data']['txs']
        if data_txs:
            for data in data_txs:
                decoded_data = base64.b64decode(data)
                pprint(decoded_data)
                print('-' * 80)
        else:
            print('The block`s data.txs is empty')
    except Exception:
        error = converted_block_data.get('error')
        if type(error) != dict:
            print(error.capitalize())
        else:
            message = error['message']
            message_description = error['data']
            print(f'{message}: {message_description}')


if __name__ == '__main__':
    get_block_data(11260637)
