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


import os
from judini.codegpt.agent import Agent

def Completion():

	prompt = input("ask me something about python")

	# Load agent credentials
	codegpt_api_key= os.getenv("CODEGPT_API_KEY")
    codegpt_agent_id= os.getenv("CODEGPT_AGENT_ID")

	# Create an agent instance
    agent_instance = Agent(api_key=codegpt_api_key, agent_id=codegpt_agent_id)

	#stream can be True or False
	response = agent_instance.completion(prompt, stream=True)

	return  response


```

## Changelog

[Changelog](https://github.com/JudiniLabs/judini-python/blob/main/CHANGELOG.md)

## Contributors

[@kevinzeladacl](https://github.com/kevinzeladacl)
