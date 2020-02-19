import json

import requests


class ITest:

    @staticmethod
    def local_server_up(server__url):
        response = requests.get(server_url)
        response1 = requests.get(server_url)
        return response.status_code == 500

    @staticmethod
    def _local_server_up(server_url):
        response = requests.get(server_url)
        return response.status_code == 200

    @staticmethod
    def do_request(server_url, source, file='', model='', mode='', data='', domain='', lang='', dictionary='',
                   force=0, param=''):
        body = {
            "source": source,
            "file": file,
            "data": data,
            "domain": domain,
            "model": model,
            "mode": mode,
            "dictionary": dictionary,
            "lang": lang,
            "force": force,
            "param": param
        }
        payload = json.dumps(body)
        header = {"Content-Type": "application/json"}
        response = requests.post(server_url, data=payload, headers=header)
        if response.status_code != 200:
            return False

        return response
