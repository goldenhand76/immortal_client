import requests

class ImmortalClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_status(self):
        url = f"{self.base_url}/status"
        response = requests.get(url)
        return response.json()

    # Add more methods to interact with your service as needed