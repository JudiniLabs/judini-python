
# Judini Python Package 0.0.16

  

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
 
import os

from judini.codegpt.agent import Agent

 
 
def  main():

	# Load API key and agent ID from environment variables
	codegpt_api_key = os.getenv("CODEGPT_API_KEY")
	codegpt_agent_id = os.getenv("CODEGPT_AGENT_ID")

	# Create an agent instance using the provided credentials
	agent_instance = Agent(api_key=codegpt_api_key, agent_id=codegpt_agent_id)

	# Get user input
	prompt =  input("Ask the agent something: ")  

	# Use the chat_completion method from the agent instance
	# This uses asynchronous programming due to the 'async' keyword
	# Typically, you'd run this inside an event loop
	# Here's a simple example using asyncio
	responses = asyncio.run(agent_instance.chat_completion(prompt, stream=True))
	for response in responses:
		print(response)


if  __name__  ==  "__main__":
	main()

  
  
  

```

 ## Examples

  

[FastAPI](https://github.com/JudiniLabs/judini-python/blob/main/examples/fastapi/fastapi.md)

   

## Changelog

  

[Changelog](https://github.com/JudiniLabs/judini-python/blob/main/CHANGELOG.md)

  

## Contributors

  

[@kevinzeladacl](https://github.com/kevinzeladacl)
