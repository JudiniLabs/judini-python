import os
import json
import aiohttp
import asyncio
import requests

url_server = "https://api.codegpt.co"
url_documentation = "https://developers.codegpt.co"


class CodeGPT:
    def __init__(self, api_key):
        self.api_key = api_key


    def me(self):
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }

            url = url_server + "/v1/users/me"
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                error_message = f"API Response was: {response.status_code} {response.reason} {url_documentation}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")



