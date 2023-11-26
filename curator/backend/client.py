import json
import requests

from curator.backend import NewsRequestInput


class Client:
    def __init__(self, host: str = 'http://localhost:8080/'):
        self.host = host

    def create_and_send_newsletter(self, user_info: NewsRequestInput,):
        response = requests.request(
            'POST',
            self.host + 'create_and_send_newsletter',
            json={'email': user_info.email,
                  'mode': user_info.mode,
                  'tone': user_info.tone,
                  'length': user_info.length}
        )
        return json.loads(response.content)
