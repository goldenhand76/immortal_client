import requests

class ImmortalClient:
    def __init__(self, base_url, kafka_host):
        self.base_url = base_url
        self.kafka_host = kafka_host

    def get_status(self):
        url = f"{self.base_url}/kafka-host"
        response = requests.post(url, json={"address": self.kafka_host})
        if response.status_code != 200:
            raise Exception()
        return response.json()

    # Add more methods to interact with your service as needed