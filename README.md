
# Judini Python Package 0.0.21
The Judini Python library provides convenient access to the CodeGPT by Judini REST API from any Python 3.7+ application. The library includes type definitions for all request params and response fields, and offers both synchronous and asynchronous clients.

  

## Documentation
The API documentation can be found [Here](https://developers.codegpt.co).

  
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

  
### Import Judini SDK
```python
import os
from src.judini.codegpt.codegpt import CodeGPT
from src.judini.codegpt.agent import Agent
from src.judini.codegpt.chat import Completion
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Retrieve the CodeGPT API key from environment variables
CODEGPT_API_KEY = os.getenv("CODEGPT_API_KEY")

```
### My data
````python  
def getMyData():
    """
    Retrieves personal data associated with the current CodeGPT instance.
    Returns: 
        A response object containing the user's data.
    """
    codegpt = CodeGPT(CODEGPT_API_KEY)
    return codegpt.me()

# Example
my_data = getMyData()
print(my_data)
````

### All Agent
````python  
def getAllAgent():
    """
    Retrieves a list of all available agents from the CodeGPT service.
    Returns:
        A list of agents.
    """
    agent = Agent(CODEGPT_API_KEY)
    return agent.getAll()

# Example
my_agents = getAllAgent()
print(my_agents)
````

### Get Agent by ID
````python  
def getAgentById(agent_id):
    """
    Retrieves details of a specific agent by its ID.
    Parameters:
        agent_id (str): The ID of the agent to retrieve.
    Returns:
        Details of the specified agent.
    """
    agent = Agent(CODEGPT_API_KEY)
    return agent.getAgentById(agent_id)

# Example
AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
my_agent = getAgentById(AGENT_ID)
print(my_agent)
````

### Update Agent Info
````python
def updateAgent(agent_id, data):
    """
    Updates the information of a specific agent.
    Parameters:
        agent_id (str): The ID of the agent to update.
        data (dict): The data to update the agent with.
    Returns:
        The updated agent information.
    """
    agent = Agent(CODEGPT_API_KEY)
    return agent.update(agent_id, data)

# Example
AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
new_data = {
    'status': 'published',
    'name': 'My Super Agent',
    'documentId': [],
    'description': 'This is a super Agent',
    'prompt': 'Example of Prompt.',
    'topk': 100,
    'temperature': 0.0,
    'model': 'gpt-3.5-turbo',
    'welcome': '',
    'maxTokens': None,
}
update = updateAgent(AGENT_ID, new_data)
print (update)
````

### Link Document to Agent
````python
def linkDocument(agent_id, documentId):
    """
    Links a document to a specific agent.
    Parameters:
        agent_id (str): The ID of the agent to link the document to.
        documentId (str): The ID of the document to link.
    Returns:
        Response object indicating the result of the operation.
    """
    agent = Agent(CODEGPT_API_KEY)
    return agent.linkDocument(agent_id, documentId)

# Example
AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
documentId = 'YOUR-ID-DOCUMENT'
link_document = linkDocument(AGENT_ID, documentId)
print(link_document)
````

### Unlink Document to Agent
````python
def unlinkDocument(agent_id, documentId):
    """
    Unlinks a document from a specific agent.
    Parameters:
        agent_id (str): The ID of the agent to unlink the document from.
        documentId (str): The ID of the document to unlink.
    Returns:
        Response object indicating the result of the operation.
    """
    agent = Agent(CODEGPT_API_KEY)
    return agent.unlinkDocument(agent_id, documentId)

# Example
AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
documentId = 'YOUR-ID-DOCUMENT'
unlink_document = unlinkDocument(AGENT_ID, documentId)
print(unlink_document)
````  

### Chat Completion
````python
def chat_completion(agent_id, prompt):
    """
    Generates a chat completion using a specific agent.
    Parameters:
        agent_id (str): The ID of the agent to use for the chat.
    prompt (dict): The chat prompt.
    Returns:
        The chat completion result.
    """
    completion = Completion(CODEGPT_API_KEY)
    return completion.create(agent_id, prompt)
    
# Example
AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
prompt = {"role": "user", "content": "What is the meaning of life?"}
chat = chat_completion(AGENT_ID, prompt)
print(chat)
````

### Chat Completion with Stream
````python
def chat_completion_stream(agent_id, prompt):
    """
    Generates a streaming chat completion using a specific agent.
    Parameters:
        agent_id (str): The ID of the agent to use for the chat.
        prompt (dict): The chat prompt.
    Returns:
        A stream of chat completion results.
    """
    completion = Completion(CODEGPT_API_KEY)
    return completion.create(agent_id, prompt, stream=True) # stream must be "True"

#example
AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
prompt = {"role": "user", "content": "What is the meaning of life?"}
stream = chat_completion_stream(AGENT_ID,prompt)

for chunk in stream:
    if chunk is not None:
        print("data:" + chunk)
        
````

### Get All Document
````python
def getAllDocument():
    """
    Retrieves info of all document files. 
    Returns: 
        A response object containing the document's data.
    """
    document = Document(CODEGPT_API_KEY)
    return document.getAll()

#example
my_documents = getAllDocument()
print(my_documents)
````  
### Get by ID Document
````python
def getDocumentById(documentId):
    """
    Retrieves info associated with the documentId. 
    Returns: 
        A response object containing the document's data.
    """
    document = Document(CODEGPT_API_KEY)
    return document.getDocumentById(documentId)

#example
documentId = 'YOUR-ID-DOCUMENT'
my_document = getDocumentById()
print(my_document)
````  


### Delete Document
````python
def deleteDocument(documentId):
    """
    Delete document associated with the documentId. 
    Returns: 
        A response object containing the document's data.
    """
    document = Document(CODEGPT_API_KEY)
    return document.delete(documentId)

#example
documentId = 'YOUR-ID-DOCUMENT'
my_document = delete(documentId)
print(my_document)
````  

### Load Document
````python
def loadDocument():
    """
    Load document file.
    Returns: 
        A response object containing the document's data.
    """
    document = Document(CODEGPT_API_KEY)
    return document.load()

#example
file = "example.txt" # path of your file
my_documents = loadDocument(file)
print(my_documents)
````  
### Training Document
````python
def trainingDocument(documentId):
    """
    Training document file.
    Returns: 
        A response object containing the document's data.
    """
    document = Document(CODEGPT_API_KEY)
    return document.training(documentId)

#example
documentId = 'YOUR-ID-DOCUMENT'
document_to_training = trainingDocument(documentId)
print(document_to_training)
````  

### Load and Training Document
````python
def loadToTrainingDocument(file):
    """
    Load and Training document file.
    Returns: 
        A response object containing the document's data.
    """
    document = Document(CODEGPT_API_KEY)
    return document.loadAndTraining(file)

#example
file = "example.txt" # path of your file
document = loadToTrainingDocument(file)
print(document)
````  

## MORE EXAMPLES
You can view examples in our [Cookbook Repository](https://github.com/judinilabs/cookbook/)

## Changelog
[Changelog](https://github.com/JudiniLabs/judini-python/blob/main/CHANGELOG.md)

## Contributors
[@davila7](https://github.com/davila7)
[@kevinzeladacl](https://github.com/kevinzeladacl)
