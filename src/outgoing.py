import requests
import json


def send_request(data_json: dict, config: dict):
    '''
    Sends the data_json as a POST request to the location specified in the
    config.
    '''
    r = requests.post('http://httpbin.org/post', data=json.dumps(data_json))
    print(r.text)
