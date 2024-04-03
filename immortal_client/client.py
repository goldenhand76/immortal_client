import requests

class ImmortalClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_status(self, address):
        url = f"{self.base_url}/kafka-setup"
        response = requests.post(url, json={"address": address})
        if response.status_code != 200:
            raise Exception()
        return response.json()

    # Add more methods to interact with your service as needed