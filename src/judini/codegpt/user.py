import requests

base_url = "https://api-beta.codegpt.co/api/v1/"

class CodeGPT:
    def __init__(self, api_key):
        self.api_key = api_key


    def me(self):
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }

            url = base_url + "/user"
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                error_message = f"API Response was: {response.status_code} {response.reason}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")



