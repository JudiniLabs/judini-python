import requests
import aiohttp
import json
from dotenv import load_dotenv
import os
load_dotenv()

class Agent:
    def __init__(self, api_key, agent_id):
        self.api_key = api_key
        self.agent_id = agent_id

    def set_api_key(self, api_key):
        self.api_key = api_key

    def set_agent_id(self, agent_id):
        self.agent_id = agent_id

    async def get_async_response(self, url, data, headers):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data, headers=headers) as response:
                return await response.text()

    async def completion(self, prompt, stream=False):
        # Headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        # Endpoint
        url = f'https://playground.judini.ai/api/v1/agent/{self.agent_id}'
        data = {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = ''
        if not stream:
            try:
                response = requests.post(url, json=data, headers=headers)
                tokens = ''
                error = ''
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        raw_data = chunk.decode('utf-8').replace("data: ", '')
                        if raw_data != "":
                            lines = raw_data.strip().splitlines()
                            for line in lines:
                                line = line.strip()
                                if line and line != "[DONE]":
                                    try:
                                        json_object = json.loads(line)
                                        result = json_object['data']
                                        result = result.replace("\n", "")
                                        tokens += result
                                    except json.JSONDecodeError:
                                        error = line
                return tokens
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
        else:
            try:
                response = await self.get_async_response(url, json.dumps(data), headers)
                return response
            except Exception as e:
                print(f"An error occurred: {e}")
