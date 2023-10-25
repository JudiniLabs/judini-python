import os
import json
import aiohttp
import asyncio
import requests

url_server = "https://api.codegpt.co"
url_documentation = "https://docs.codegpt.co/docs/tutorial-ai-providers/judini"


class Agent:
    def __init__(self, api_key, agent_id=""):
        self.api_key = api_key
        self.agent_id = agent_id
        self.is_streaming = False

    def is_loading(self):
        return self.is_streaming

    def stop_streaming(self):
        self.is_streaming = False

    async def get(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        url = f"{url_server}/v1/agent/{self.agent_id}" if self.agent_id else f"{url_server}/v1/agent"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                error_message = f"JUDINI: API Response was: {response.status_code} {response.reason} {url_documentation}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")

    async def update(self, data):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        url = f"{url_server}/v1/agent/{self.agent_id}"
        try:
            response = requests.patch(url, json=data, headers=headers)
            if response.status_code != 200:
                error_message = f"JUDINI: API Response was: {response.status_code} {response.reason} {url_documentation}"
                raise Exception(error_message)
            else:
                return response.json()

        except Exception as e:
            print(f"An error occurred: {e}")

    async def chat_completion(self, prompt, stream=False):
        # Define los valores de headers, messages y la nueva URL
        headers = {
            "Content-Type": "application/json",
            "media_type": "text/event-stream",
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            prompt[0]
        except:
            prompt = [prompt]

        messages = {
            "agent": self.agent_id,
            "messages": prompt
        }

        url = f"{url_server}/v1/completion"

        full_response = ""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=messages, headers=headers) as response:
                    if response.status != 200:
                        error_message = f"JUDINI: API Response was: {response.status} {response.reason} {'https://docs.codegpt.co/docs/tutorial-ai-providers/judini'}"
                        raise Exception(error_message)

                    async for line in response.content.iter_any():
                        text = line.decode(
                            'utf-8').replace("data:", '').strip()
                        if text == "[DONE]":
                            self.is_streaming = False
                            break
                        if stream:
                            yield text + '\n'
                        else:
                            full_response += text

                    if not stream:
                        yield full_response  # Enviar la respuesta completa

        except Exception as e:
            print(f"An error occurred: {e}")
            self.is_streaming = False
