
# Judini Python Package 0.1.5
The Judini Python library provides convenient access to CodeGPT's Judini REST API from any Python 3.7+ application. The library includes type definitions for all request parameters and response fields, and offers synchronous and asynchronous clients.

## Documentation
The API documentation can be found [Here](https://developers.codegpt.co).

## Install
To install the package, simply run the following command:

```bash
pip install judini
```

## How to get API KEY and AGENT ID
1. Create an account at https://app.codegpt.co
2. Get your **CodeGPT Api Key** from the Api Keys menu
3. copy and replace your **CODEGPT API KEY**
4. Create an Agent and get your **AGENT ID**
5. Copy and replace your **AGENT KEY**

  
## How to Usage
### Import Judini SDK
```python
import os
from judini.codegpt.agent import Agent
from judini.codegpt.chat import Completion
from judini.codegpt.document import Document
import dotenv

# Load environment variables
dotenv.load_dotenv()

# CodeGPT Environment Variables API Key
CODEGPT_API_KEY = os.getenv("CODEGPT_API_KEY")
AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
```

### Chat Completion
```python
def chat_completion(agent_id, messages):
    """
    Chat completion by Agent ID
    Parameters:
        agent_id (str): Agent ID
        messages (dict): Messages { "role": "user", "content": "user prompt" }
    Returns:
        Chat completion result
    """
    completion  =  Completion(CODEGPT_API_KEY)
    return  completion.create(agent_id, messages)
    
# Example
messages = {"role": "user", "content": "What is the meaning of life?"}
chat = chat_completion(AGENT_ID, messages)
print(chat)
```

### All Agent
```python  
def getAllAgent():
    """
    Retrieves a list of all available agents
    Returns:
        A list of agents.
    """
    agent = Agent(CODEGPT_API_KEY)
    return agent.getAll()

# Example
my_agents = getAllAgent()
print(my_agents)
```

### Get agent data by ID
```python  
def getAgentById(agent_id):
    """
    Retrieves details of a specific agent by Agent ID
    Parameters:
        agent_id (str): Agent ID
    Returns:
        Agent details
    """
    agent  =  Agent(CODEGPT_API_KEY)
    return  agent.getAgentById(agent_id)

# Example
AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
my_agent = getAgentById(AGENT_ID)
print(my_agent)
```

### Update Agent
```python
def updateAgent(agent_id, data):
    """
    Updates information for a specific agent.
    Parameters:
        agent_id (str): Agent ID
        data (dict) : Agent data to update
    Returns:
        Updated agent details
    """
    agent  =  Agent(CODEGPT_API_KEY)
    return  agent.update(agent_id, data)

# Example
AGENT_ID  =  os.getenv("CODEGPT_AGENT_ID")
new_data  = {
    'status': 'published',
    'name': 'DevSuper2',
    'documentId': [],
    'description': 'Dev Super 2',
    'prompt': 'You are an expert senior multilanguage programmer and you must help with the code and questions they ask of you.',
    'topk': 100,
    'temperature': 0.0,
    'model': 'gpt-3.5-turbo',
    'welcome': '',
    'maxTokens': None,
}
update = updateAgent(AGENT_ID, new_data)
print (update)
```

### Link document to an agent
```python
def linkDocument(agent_id, documentId):
    """
    Links a document to a specific agent.
    Parameters:
        agent_id (str): Agent ID
        documentId (str): Document ID to link.
    Returns:
        Response object indicating the result of the operation.
    """
    agent  =  Agent(CODEGPT_API_KEY)
    return  agent.linkDocument(agent_id, documentId)

# Example
AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
documentId = '123456' # replace with your document id
link_document = linkDocument(AGENT_ID, documentId)
print(link_document)
```

### Unlink document to an agent
```python
def unlinkDocument(agent_id, documentId):
    """
    Unlinks a document from a specific agent.
    Parameters:
        agent_id (str): Agent ID to unlink the document from.
        documentId (str): Document ID to unlink.
    Returns:
        Response object indicating the result of the operation.
    """
    agent = Agent(CODEGPT_API_KEY)
    return agent.unlinkDocument(agent_id, documentId)

# Example
AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
documentId = '123456' # replace with your document id
unlink_document = unlinkDocument(AGENT_ID, documentId)
print(unlink_document)
```

### Get All Document
```python
def getAllDocument():
    """
    Get all documents
    Returns: 
        An object with all the account documents
    """
    document = Document(CODEGPT_API_KEY)
    return document.getAll()

#example
my_documents = getAllDocument()
print(my_documents)
```  

### Get Document by ID
```python
def getDocumentById(documentId):
    """
    Get Document by ID
    Returns: 
        A response object that contains the document data
    """
    document = Document(CODEGPT_API_KEY)
    return document.getDocumentById(documentId)

#example
documentId = 'YOUR_DOCUMENT_ID'
my_document = getDocumentById()
print(my_document)
```  

### Load Document
```python
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
```  

### Training Document
```python
def trainingDocument(documentId):
    """
    Training document file.
    Returns: 
        A response object containing the document's data.
    """
    document = Document(CODEGPT_API_KEY)
    return document.training(documentId)

#example
documentId = 'YOUR_DOCUMENT_ID'
document_to_training = trainingDocument(documentId)
print(document_to_training)
```  

### Load and Training Document
```python
def loadToTrainingDocument(file):
    """
    Load and Training a Document
    Returns: 
        A response object that contains the document data
    """
    document = Document(CODEGPT_API_KEY)
    return document.loadAndTraining(file)

#example
file = "example.txt" # path to your file
document = loadToTrainingDocument(file)
print(document)
```  

## MORE EXAMPLES
You can review more examples in our [Cookbook Repository](https://github.com/judinilabs/cookbook/)

## Changelog
[Changelog](https://github.com/JudiniLabs/judini-python/blob/main/CHANGELOG.md)