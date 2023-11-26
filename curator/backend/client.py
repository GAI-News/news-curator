import json
from PIL.Image import Image
import requests
from typing import List


class Client:
    def __init__(self, host: str = 'http://localhost:8080/'):
        self.host = host

    def retrieve_news(self) -> List[str]:
        response = requests.request('POST', self.host + 'retrieve_news')
        return json.loads(response.content)

    def cluster_news(self) -> List[str]:
        response = requests.request('POST', self.host + 'cluster_news')
        return json.loads(response.content)
