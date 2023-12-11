import os
import json
import aiohttp
import asyncio
import requests


url_server = "https://api.codegpt.co"
url_documentation = "https://developers.codegpt.co"

class Completion:
    def __init__(self, api_key):
        self.api_key = api_key


    def create(self, agent_id, prompt, stream=False):
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
                "agent": agent_id,
                "messages": prompt,
                "stream": stream,
            }

            url = f"{url_server}/v1/completion"
            if stream is False:
                try:
                    response = requests.post(url, json=messages, headers=headers)
                    if response.status_code != 200:
                        error_message = f"API Response was: {response.status} {response.reason} {url_documentation}"
                        raise Exception(error_message)
                    

                    return response.json().split('data: ')[1]
                
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                try:
                    response = requests.post(url, json=messages, headers=headers)
                    if response.status_code != 200:
                        error_message = f"API Response was: {response.status} {response.reason} {url_documentation}"
                        raise Exception(error_message)

                    return response.text.split('data: ')
                
                except Exception as e:
                    print(f"An error occurred: {e}")






# #######
# def chat_completion(self, prompt, stream=False):
#         # Define los valores de headers, messages y la nueva URL
#         headers = {
#             "Content-Type": "application/json",
#             "media_type": "text/event-stream",
#             "Authorization": f"Bearer {self.api_key}"
#         }

#         try:
#             prompt[0]
#         except:
#             prompt = [prompt]

#         messages = {
#             "agent": self.agent_id,
#             "messages": prompt
#         }

#         url = f"{url_server}/v1/completion"

#         full_response = ""
#         try:
#             async with aiohttp.ClientSession() as session:
#                 async with session.post(url, json=messages, headers=headers) as response:
#                     if response.status != 200:
#                         error_message = f"API Response was: {response.status} {response.reason} {url_documentation}"
#                         raise Exception(error_message)

#                     import pdb; pdb.set_trace()
#                     async for line in response.content.iter_any():
#                         text = line.decode(
#                             'utf-8').replace("data:", '').strip()
#                         if text == "[DONE]":
#                             self.is_streaming = False
#                             break
#                         if stream:
#                             yield text + '\n'
#                         else:
#                             full_response += text

#                     if not stream:
#                         yield full_response  # Enviar la respuesta completa

#         except Exception as e:
#             print(f"An error occurred: {e}")
#             self.is_streaming = False
