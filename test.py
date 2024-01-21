import os
from judini.codegpt.user import CodeGPT
from src.judini.codegpt.agent import Agent
from src.judini.codegpt.chat import Completion
from src.judini.codegpt.document import Document

import dotenv

dotenv.load_dotenv()

CODEGPT_API_KEY = os.getenv("CODEGPT_API_KEY")


# Retrieve the CodeGPT API key from environment variables


def getMyData():
	# Define the CodeGPT instance
	codegpt = CodeGPT(CODEGPT_API_KEY)
	#return my data
	return codegpt.me()

def getAllAgent():
    # Define the Agent instance
    agent = Agent(CODEGPT_API_KEY)
    #return All Agents
    return agent.getAll()

def getAgentById(agent_id):
    # Define the Agent instance
    agent = Agent(CODEGPT_API_KEY)
    #return Agent by id
    return agent.getAgentById(agent_id)

def updateAgent(agent_id,data):
     # Define the Agent instance
    agent = Agent(CODEGPT_API_KEY)
    #return Agent Update
    return agent.update(agent_id,data)

def linkDocument(agent_id,documentId):
     # Define the Agent instance
    agent = Agent(CODEGPT_API_KEY)
    #return Agent Update with document added
    return agent.linkDocument(agent_id,documentId)

def unlinkDocument(agent_id,documentId):
     # Define the Agent instance
    agent = Agent(CODEGPT_API_KEY)
    #return agent with document removed
    return agent.unlinkDocument(agent_id,documentId)

def chat_completion(agent_id,prompt):
    completion = Completion(CODEGPT_API_KEY)
    return completion.create( agent_id,prompt)

def chat_completion_stream(agent_id,prompt):
    completion = Completion(CODEGPT_API_KEY)
    return completion.create( agent_id,prompt,stream=True)

def getAllDocument():
    # Define the Agent instance
    document = Document(CODEGPT_API_KEY)
    #return All Agents
    return document.getAll()

def getDocumentById(documentId):
    # Define the Agent instance
    document = Document(CODEGPT_API_KEY)
    #return All Agents
    return document.getDocumentById(documentId)

def deleteDocument(file):
    # Define the Agent instance
    document = Document(CODEGPT_API_KEY)
    #return All Agents
    return document.delete(file)

def loadDocument(file):
    # Define the Agent instance
    document = Document(CODEGPT_API_KEY)
    #return All Agents
    return document.load(file)

def trainingDocument(file):
    # Define the Agent instance
    document = Document(CODEGPT_API_KEY)
    #return All Agents
    return document.training(file)

def loadToTrainingDocument(file):
    # Define the Agent instance
    document = Document(CODEGPT_API_KEY)
    #return All Agents
    return document.loadAndTraining(file)

#### return
# #example 1
# my_data = getMyData()
# #example 2
# my_agents = getAllAgent()
# #example 3
# AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
# my_agent = getAgentById(AGENT_ID)
# #example 4
# AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
# new_data =  {      
#         'status': 'published', 
#         'name': 'DevSuper2', 
#         'documentId': [], 
#         'description': 'Dev Super 2', 
#         'prompt': 'Eres un Experto programador multilenguaje senior y debes ayudar con el codigo y preguntas que te pidan.', 
#         'topk': 100, 
#         'temperature': 0.0, 
#         'model': 'gpt-3.5-turbo', 
#         'welcome': '', 
#         'maxTokens': None, 
# }
# update = updateAgent(AGENT_ID,new_data)

# # example 5
# AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
# documentId = '3a06c023-4bdb-44be-8af4-6278b3a661fb'
# link_document = linkDocument(AGENT_ID,documentId)
# print(link_document)

#example 6
AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
documentId = '3a06c023-4bdb-44be-8af4-6278b3a661fb'
unlink_document = unlinkDocument(AGENT_ID,documentId)
print(unlink_document)

# #example 7
# AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
# prompt = {"role": "user", "content": "What is the meaning of life?"}
# chat = chat_completion(AGENT_ID,prompt)

# #example 8
# AGENT_ID = os.getenv("CODEGPT_AGENT_ID")
# prompt = {"role": "user", "content": "What is the meaning of life?"}
# chat = chat_completion_stream(AGENT_ID,prompt)

# for chunk in chat:
#     if chunk is not None:
#         print("data: " + chunk)

# #example 9
# my_documents = getAllDocument()
# print(my_documents)

# #example 10
# documentId = '3a06c023-4bdb-44be-8af4-6278b3a661fb'
# my_document = getDocumentById(documentId)
# print(my_document)

# #example 11
# documentId = '3a06c023-4bdb-44be-8af4-6278b3a661fb'
# delete_document = deleteDocument(documentId)
# print(delete_document)

# #example 12 (fail)
# file = 'example.txt'
# document = loadDocument(file)
# print(document)

# # #example 13 (fail)
# documentId = '3a06c023-4bdb-44be-8af4-6278b3a661fb'
# document_to_training = trainingDocument(documentId)
# print(my_documents)

# # #example 14 (fail)
# file = 'example.txt'
# document = loadToTrainingDocument(file)
# print(document)

