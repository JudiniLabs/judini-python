
# Judini Python Package
The Judini Python library provides convenient access to CodeGPT's Judini REST API from any Python 3.7+ application. The library includes type definitions for all requests parameters and response fields, and offers synchronous and asynchronous clients.

## Documentation
The API documentation can be found [Here](https://developers.codegpt.co).

## Install
To install the package, simply run the following command:

```bash
pip install judini
```

## How to get your keys
1. Create an account at https://app.codegpt.co
2. Get your **CodeGPT Api Key** and **Org ID** from the [Apikeys menu](https://app.codegpt.co/en/apikeys)
  
## How to use

### Chat Completion

```python
from judini import CodeGPTPlus
codegpt = CodeGPTPlus(api_key=CODEGPT_API_KEY, org_id=ORG_ID)

AGENT_ID = "0000000-0000-0000-0000-000000000000"
messages = [{"role": "user", "content": "What is the meaning of life?"}]

# No streaming
chat = codegpt.chat_completion(agent_id=AGENT_ID,
                               messages=messages)
print(chat)

# Streaming
for chunk in codegpt.chat_completion(agent_id=AGENT_ID,
...                                  messages=messages,
...                                  stream=True):
    print(chunk, end="")
```

### Agents
#### List all agents
```python
from judini import CodeGPTPlus
codegpt = CodeGPTPlus(api_key=CODEGPT_API_KEY, org_id=ORG_ID)
codegpt.get_agents()
>> [Agent(id='0000000-0000-0000-0000-000000000000', ...),
>>  Agent(id='0000000-0000-0000-0000-000000000001', ...)]
```

#### Get agent by ID
```python  
from judini import CodeGPTPlus
codegpt = CodeGPTPlus(api_key=CODEGPT_API_KEY, org_id=ORG_ID)
agent = codegpt.get_agent(agent_id='0000000-0000-0000-0000-000000000000')
agent
>> Agent(id='0000000-0000-0000-0000-000000000000',
>>       name='Agent name', model='gpt-3.5-turbo',
>>       prompt='You are a helpful assistant.',
>>       welcome='Hello, how can I help you?',
>>       ...)
```

#### Create Agent
```python
from judini import CodeGPTPlus
codegpt = CodeGPTPlus(api_key=CODEGPT_API_KEY, org_id=ORG_ID)
codegpt.create_agent(name='Agent name', model='gpt-3.5-turbo',
...                  prompt='You are a helpful assistant.',
...                  welcome='Hello, how can I help you?')
>> Agent(id='0000000-0000-0000-0000-000000000000',
>>       name='Agent name', model='gpt-3.5-turbo', ...)
```

#### Update Agent info
```python
from judini import CodeGPTPlus
codegpt = CodeGPTPlus(api_key=CODEGPT_API_KEY, org_id=ORG_ID)
codegpt.update_agent(agent_id='0000000-0000-0000-0000-000000000000',
...                  name='Agent name updated',
...                  model='gpt-4-turbo-preview')
>> Agent(id='0000000-0000-0000-0000-000000000000',
>>       name='Agent name updated', model='gpt-3.5-turbo', ...)                    
```

#### Update Agent documents
```python
from judini import CodeGPTPlus
codegpt = CodeGPTPlus(api_key=CODEGPT_API_KEY, org_id=ORG_ID)
codegpt.update_agent_documents(agent_id='0000000-0000-0000-0000-000000000000',
...                            document_ids=[DOCUMENT_ID_1, DOCUMENT_ID_2])
>> "Agent documents updated successfully"
```

#### Delete Agent
```python
from judini import CodeGPTPlus
codegpt = CodeGPTPlus(api_key=CODEGPT_API_KEY, org_id=ORG_ID)
codegpt.delete_agent('0000000-0000-0000-0000-000000000000')
>> "Agent deleted successfully"
```


### Documents
#### List all documents
```python
from judini import CodeGPTPlus
codegpt = CodeGPTPlus(api_key=CODEGPT_API_KEY, org_id=ORG_ID)
codegpt.get_documents()
>> [Document(id='0000000-0000-0000-0000-000000000000', ...),
>>  Document(id='0000000-0000-0000-0000-000000000001', ...)]
```

#### Get document by ID
```python
from judini import CodeGPTPlus
codegpt = CodeGPTPlus(api_key=CODEGPT_API_KEY, org_id=ORG_ID)
document = codegpt.get_document_by_id('0000000-0000-0000-0000-000000000000')
document
>> Document(id='0000000-0000-0000-0000-000000000000',
>>          user_id='...',
>>          name='My Document',
>>          metadata='...',
>>          content='Document content', ...)
```

#### Upload a document
**Currently, only text documents are supported**
```python	
from judini import CodeGPTPlus
codegpt = CodeGPTPlus(api_key=CODEGPT_API_KEY, org_id=ORG_ID)
codegpt.upload_document('path/to/file.txt', generate_metadata=False)
>> {'id': '0000000-0000-0000-0000-000000000000'}
```

#### Update document metadata
```python
from judini import CodeGPTPlus
codegpt = CodeGPTPlus(api_key=CODEGPT_API_KEY, org_id=ORG_ID)
codegpt.update_document_metadata(id='0000000-0000-0000-0000-000000000000',
...                              title='My Document Updated',)
>> "Document metadata updated successfully"
```

#### Delete a document
```python
from judini import CodeGPTPlus
codegpt = CodeGPTPlus(api_key=CODEGPT_API_KEY, org_id=ORG_ID)
codegpt.delete_document('0000000-0000-0000-0000-000000000000')
>> "Document deleted successfully"
```

## MORE EXAMPLES
You can review more examples in our [Cookbook Repository](https://github.com/judinilabs/cookbook/)

## Changelog
[Changelog](https://github.com/JudiniLabs/judini-python/blob/main/CHANGELOG.md)