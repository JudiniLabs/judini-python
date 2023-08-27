# Judini Python Package

This package provides you with an easy way to interact with the Judini API in your Python applications.

## Install

To install the package, simply run the following command:

```bash

pip  install  judini

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
import os
from judini.codegpt.agent
import Agent

async  def  main():
	# Load agent credentials
	api_key = os.getenv('CODEGPT_API_KEY')
	agent_id = os.getenv('CODEGPT_AGENT_ID')

	# Create an agent instance
	agent = Agent(api_key, agent_id)

	# Define the test message
	prompt = "Can you help me?"

	# Test with stream=False
	response = await agent.completion(prompt, stream=False) print(f"Response with stream=False: {response}")

	# Test with stream=True
	response = await agent.completion(prompt, stream=True) print(f"Response with stream=True: {response}")

if __name__ == "__main__":
	asyncio.run(main())

```

## Changelog

[Changelog](https://github.com/JudiniLabs/judini-python/blob/main/CHANGELOG.md)

## Contributors

[@kevinzeladacl](https://github.com/kevinzeladacl)
