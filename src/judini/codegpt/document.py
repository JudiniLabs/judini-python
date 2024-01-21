import requests

base_url = "https://api-beta.codegpt.co/api/v1"

class Document:
    def __init__(self, api_key):
        self.api_key = api_key


    def getAll(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        url = f"{base_url}/document"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                error_message = f"API Response was: {response.status_code} {response.reason} {url_documentation}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")

    def getDocumentById(self,documentId):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        url = f"{base_url}/document/"+documentId

        try:
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                error_message = f"API Response was: {response.status_code} {response.reason} {url_documentation}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")
    
    def delete(self,documentId):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        url = f"{base_url}/document/"+documentId

        try:
            response = requests.delete(url, headers=headers)
            if response.status_code != 200:
                error_message = f"API Response was: {response.status_code} {response.reason} {url_documentation}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")

    def load(self,file):
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        url = f"{base_url}/document/load"

        try:
            with open(file, "rb") as f:
                response = requests.post(url,files={"file" : f},headers=headers)
            if response.status_code != 200:
                error_message = f"API Response was: {response.status_code} {response} {url_documentation}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")


    def training(self,documentId):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        url = f"{base_url}/document/training/{documentId}"

        try:
            response = requests.post(url, headers=headers)
            if response.status_code != 200:
                error_message = f"API Response was: {response.status_code} {response.reason} {url_documentation}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")



    def loadAndTraining(self,file):
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        url = f"{base_url}/document/load-and-training"

        try:
            with open(file, "rb") as f:
                response = requests.post(url, files={"file" : f},headers=headers)

            if response.status_code != 200:
                error_message = f"API Response was: {response.status_code} {response} {url_documentation}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")