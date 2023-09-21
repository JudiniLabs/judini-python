import aiohttp
import json
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

class Agent:
    def __init__(self, api_key, agent_id=""):
        self.api_key = api_key
        self.agent_id = agent_id
        self.is_streaming = False

    def is_loading(self):
        return self.is_streaming

    def stop_streaming(self):
        self.is_streaming = False

    async def chat_completion(self, prompt, stream=False):
        # Headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        messages = [{"role": "user", "content": prompt}]

        # Endpoint
        url = f'https://plus.codegpt.co/api/v1/agent/{self.agent_id}' if self.agent_id else 'https://plus.codegpt.co/api/v1/agent'
        
        full_response = ""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json={"messages": messages}, headers=headers) as response:
                    if response.status != 200:
                        error_message = f"JUDINI: API Response was: {response.status} {response.reason} {'https://docs.codegpt.co/docs/tutorial-ai-providers/judini'}"
                        raise Exception(error_message)
                    
                    async for line in response.content.iter_any():
                        text = line.decode('utf-8').replace("data: ", '').strip()
                        if text.startswith('{"function":'):
                            yield text
                        else:
                            if text == "[DONE]":
                                self.is_streaming = False
                                break
                            try:
                                data_chunk = json.loads(text)
                                if stream:
                                    yield data_chunk['data'] + '\n'
                                else:
                                    full_response += data_chunk['data']
                            except json.JSONDecodeError:
                                pass
                    if not stream:
                        yield full_response

        except Exception as e:
            print(f"An error occurred: {e}")
            self.is_streaming = False