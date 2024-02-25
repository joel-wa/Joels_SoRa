import requests

class ServerRequest:

    def __init__(self,url) -> None:
        self.url = url

    def requestObject(self,prompt):
        response = requests.post(self.url,json=prompt)

        if response.status_code == 201:
            # print("successful")
            return response.text

        else:
            return f"Error: {response.status_code}"
