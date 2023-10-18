
# Judini Python Package 0.0.18

  

This package provides you with an easy way to interact with the Judini API in your Python applications.

  

## Install

  

To install the package, simply run the following command:

  

```bash

  

pip install judini

  

```

  

## How get API Key and AGENT ID

  

1- **CODEGPT API KEY**

  

You must go to https://plus.codegpt.co then go to configuration and go to **Configuration> Access Tokens**

  

And copy **CODEGPT API KEY**

  

2 - **CODE AGENT ID**

  

**Agent configuration > Advanced configuration > Agent ID**

  

And copy **AGENT ID**

  

## Usage

  

Below is a sample code demonstrating how to use the Judini package in your Python application:

  

```python
 
import asyncio
from judini.codegpt.agent import Agent

async def chat_example(prompt):
	CODEGPT_API_KEY = "YOUR_APIKEY"
	CODEGPT_AGENT_ID = "YOUR_AGENT_ID"

	agent_instance = Agent(api_key=CODEGPT_API_KEY, agent_id=CODEGPT_AGENT_ID)

	async for response in agent_instance.chat_completion(prompt, stream=True):
		print(response)

if __name__ == "__main__":
	text = "First president of USA?"
	prompt = {"role": "user", "content": text}
	asyncio.run(chat_example(prompt))

  
  
  

```

 ## Examples

  

[FastAPI](https://github.com/JudiniLabs/judini-python/blob/main/examples/fastapi/fastapi.md)

   

## Changelog

  

[Changelog](https://github.com/JudiniLabs/judini-python/blob/main/CHANGELOG.md)

  

## Contributors

  

[@kevinzeladacl](https://github.com/kevinzeladacl)
