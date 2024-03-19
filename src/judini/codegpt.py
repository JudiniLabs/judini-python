import os
import mimetypes
import warnings
import json
import requests
from typing import List, Dict, Literal, Optional
from .utils import handle_non_stream, handle_stream
from .types import Agent, Document, DocumentMetadata

base_url = 'https://api-beta.codegpt.co/api/v1'
JUDINI_TUTORIAL = f'{base_url}/docs'
PLAYGROUND_KEYS_URL = 'https://app.codegpt.co/en/apikeys' 

class CodeGPTPlus:
    def __init__(self,
                 api_key: Optional[str] = None,
                 org_id: Optional[str] = None,
                 base_url: str = base_url):

        if not api_key:
            api_key = os.getenv("CODEGPT_API_KEY")
            if not api_key:
                raise Exception('JUDINI: API key not found. Please set'
                                + ' the CODEGPT_API_KEY environment variable'
                                + ' or pass it as an argument.\nYou can get'
                                + ' your API key from: ' + PLAYGROUND_KEYS_URL)
        self.headers = {
            'Content-Type': 'application/json',
            'Channel' : 'SDK_PYTHON',
            'Authorization': 'Bearer ' + api_key
        }
        if not org_id:
            org_id = os.getenv("CODEGPT_ORG_ID")

        if org_id:
            self.headers['CodeGPT-Org-Id'] = org_id
        else:
            warnings.warn('\nJUDINI: Org ID not found. This could lead to'
                          + ' unexpected behavior.\nYou can get your org ID'
                          + ' from: ' + PLAYGROUND_KEYS_URL)
        
        self.is_streaming = False
        self.base_url = base_url



    #######################
    ### CHAT COMPLETION ###
    #######################
        
    def chat_completion(self, agent_id: str, messages: List[Dict[str, str]], 
               stream: bool = False) -> str:
        """
        Initiates a chat with the specified agent and handles the streaming of
        responses.

        Parameters
        ----------

        agent_id: The ID of the agent to chat with.
        messages: An array of message objects to be sent to the agent. Each
                  object should have a `role` (which can be 'system', 'user',
                  or 'assistant') and `content` which is the actual message.
        stream: Whether to stream the response or not.

        Example:
        >>> from judini import CodeGPTPlus
        >>> codegpt = CodeGPTPlus(api_key, org_id)
        >>> agent_id = '00000000-0000-0000-0000-000000000000'
        >>> messages = [{'role': 'user', 'content': 'Hello, World!'}]
        >>> codegpt.chat_completion(agent_id, messages, stream=True)
        'Hello, World!'
        """
        
        if len(messages) == 0:
            raise ValueError('JUDINI: messages array should not be empty')
        
        if not agent_id:
            raise ValueError('JUDINI: agent_id should not be empty')
        

        headers = self.headers.copy()
        headers['accept'] = 'text/event-stream'

        payload = json.dumps({
            "agentId": agent_id,
            "messages": messages,
            "stream": stream,
            "format": "text"
        })

        response = requests.post(f"{self.base_url}/chat/completions",
                                 headers=headers, data=payload,
                                 stream=stream)
        if response.status_code != 200:
            raise Exception(f'JUDINI: API Response was: {response.status_code}'
                            + f' {response.text} {JUDINI_TUTORIAL}')
        
        if stream:
            return handle_stream(response)
        else:
            return handle_non_stream(response)
        

    ##############
    ### AGENTS ###
    ##############

    def get_agents(self) -> List[Agent]:
        """
        Retrieves a list of all the agents from the CodeGPTPlus API.

        Returns an array of json objects representing agents with the following
        properties:
            id: str = The ID of the agent
            name: str = The name of the agent
            prompt: str = The prompt of the agent
            model: str = The model of the agent
            agent_documents: Optional[List[str]] = The list of documents
                                                    associated with the agent
            welcome: str = The welcome message of the agent
            pincode: Optional[str] = The pincode of the agent
            is_public: bool = Whether the agent is public or not
            agent_type: str = The type of the agent
        """

        response = requests.get(f"{self.base_url}/agent", headers=self.headers)

        if response.status_code != 200:
            raise Exception(f'JUDINI: API Response was: {response.status_code}'
                            + f' {response.text} {JUDINI_TUTORIAL}')
        
        agent_lists = response.json()
        return [Agent(**agent_dict) for agent_dict in agent_lists]
    
    def get_agent(self, agent_id: str) -> Agent:
        """
        Retrieves a specific agent from the CodeGPTPlus API.

        Parameters
        ----------
        agent_id: The ID of the agent to retrieve.

        Returns a json object representing the agent with the following
        properties:
            id: str = The ID of the agent
            name: str = The name of the agent
            prompt: str = The prompt of the agent
            model: str = The model of the agent
            agent_documents: Optional[List[str]] = The list of documents
                                                   associated with the agent
            welcome: str = The welcome message of the agent
            pincode: Optional[str] = The pincode of the agent
            is_public: bool = Whether the agent is public or not
            agent_type: str = The type of the agent
        """

        response = requests.get(f"{self.base_url}/agent/{agent_id}?populate=agent_documents",
                                 headers=self.headers)

        if response.status_code != 200:
            raise Exception(f'JUDINI: API Response was: {response.status_code}'
                            + f' {response.text} {JUDINI_TUTORIAL}')
        
        return Agent(**response.json())
    
    def create_agent(self,
                     name: str,
                     model: str="gpt-3.5-turbo",
                     prompt: str = "You are a helpful assistant.",
                     welcome: str = "Hello, how can I help you today?",
                     topk: int=3,
                     temperature: int=0.7,
                     ) -> Agent:
        """
        Creates a new agent in the CodeGPTPlus API.

        Parameters
        ----------
        name: The name of the agent.
        model: The model to be used by the agent. For example, 'gpt-3.5-turbo'.
        prompt: The prompt of the agent.
        welcome: The welcome message of the agent.
        topk: The number of elements to retrieve from the documents
        temperature: The temperature of the agent.

         Returns a json object representing the agent with the following
         properties:
            id: str = The ID of the agent
            name: str = The name of the agent
            prompt: str = The prompt of the agent
            model: str = The model of the agent
            agent_documents: Optional[List[str]] = The list of documents
                                                   associated with the agent
            welcome: str = The welcome message of the agent
            pincode: Optional[str] = The pincode of the agent
            is_public: bool = Whether the agent is public or not
            agent_type: str = The type of the agent
        """

        payload = json.dumps({
            "name": name,
            "model": model,
            "prompt": prompt,
            "welcome": welcome,
            "topk": topk,
            "temperature": temperature
        })
        response = requests.post(f"{self.base_url}/agent", headers=self.headers,
                                 data=payload)
        
        if response.status_code != 200:
            raise Exception(f'JUDINI: API Response was: {response.status_code}'
                            + f' {response.text} {JUDINI_TUTORIAL}')
        
        return Agent(**response.json())
    
    def update_agent(self,
                     agent_id: str,
                     name: Optional[str] = None,
                     model: Optional[str] = None,
                     prompt: Optional[str] = None,
                     welcome: Optional[str] = None,
                     topk: Optional[int] = None,
                     temperature: Optional[int] = None,
                     is_public: Optional[bool] = None,
                     pincode: Optional[str] = None
                     ) -> Agent:
        """
        Updates an existing agent in the CodeGPTPlus API.
        Apart from the agent ID, at least one parameter is required.

        Parameters
        ----------
        agent_id: The ID of the agent to update.
        name: (optional) The updated name of the agent.
        model: (optional) The updated model to be used by the agent.
        prompt: (optional) The updated prompt of the agent.
        welcome: (optional) The updated welcome message of the agent.
        topk: (optional) The updated number of elements to retrieve from the
                         documents
        temperature: (optional) The updated temperature of the agent.
        is_public: (optional) The updated visibility of the agent.
        pincode: (optional) The updated pincode of the agent.

         Returns a json object representing the agent with the following
         properties:
            id: str = The ID of the agent
            name: str = The name of the agent
            prompt: str = The prompt of the agent
            model: str = The model of the agent
            agent_documents: Optional[List[str]] = The list of documents
                                                   associated with the agent
            welcome: str = The welcome message of the agent
            pincode: Optional[str] = The pincode of the agent
            is_public: bool = Whether the agent is public or not
            agent_type: str = The type of the agent
        """
        
        if not agent_id:
            raise ValueError('JUDINI: agent_id should not be empty')
        
        payload = {}
        if name:
            payload['name'] = name
        if model:
            payload['model'] = model
        if prompt:
            payload['prompt'] = prompt
        if welcome:
            payload['welcome'] = welcome
        if topk:
            payload['topk'] = topk
        if temperature:
            payload['temperature'] = temperature
        if is_public:
            payload['is_public'] = is_public
        if pincode:
            payload['pincode'] = pincode

        if not payload:
            raise ValueError('JUDINI: At least one parameter must be provided')
        
        payload = json.dumps(payload)

        response = requests.patch(f"{self.base_url}/agent/{agent_id}",
                                  headers=self.headers,
                                  data=payload)
        
        if response.status_code != 200:
            raise Exception(f'JUDINI: API Response was: {response.status_code}'
                            + f' {response.text} {JUDINI_TUTORIAL}')
        
        return Agent(**response.json())
    

    def delete_agent(self, agent_id: str) -> None:
        """
        Deletes an agent from the CodeGPTPlus API.

        Parameters
        ----------
        agent_id: The ID of the agent to delete.
        """

        response = requests.delete(f"{self.base_url}/agent/{agent_id}",
                                   headers=self.headers)
        
        if response.status_code != 200:
            raise Exception(f'JUDINI: API Response was: {response.status_code}'
                            + f' {response.text} {JUDINI_TUTORIAL}')
        
        print('Agent deleted successfully')
        return
    
    def update_agent_documents(self, agent_id: str, document_ids: List[str]) -> None:
        """
        Updates the documents associated with an agent in the CodeGPTPlus API.

        Parameters
        ----------
        agent_id: The ID of the agent to update.
        document_ids: The IDs of the documents to associate with the agent.
        """
        payload = json.dumps({ "agent_documents": document_ids})
        response = requests.patch(f"{self.base_url}/agent/{agent_id}/documents",
                                  headers=self.headers,
                                  data=payload)
        
        if response.status_code != 200:
            raise Exception(f'JUDINI: API Response was: {response.status_code}'
                            + f' {response.text} {JUDINI_TUTORIAL}')
        
        print('Agent documents updated successfully')
        return 

    #################
    ### DOCUMENTS ###
    #################

    def get_documents(self) -> List[Document]:
        """
        Retrieves a list of all the documents from the CodeGPTPlus API.

        Returns an array of json objects representing documents with the
        following properties:
            id: str = The ID of the document
            user_id: str = The ID of the user who created the document
            name: str = The name of the document
            content: str = The content of the document
            file_type: str = The type of the document
            metadata: Optional[DocumentMetadata] = The metadata of the document
            tokens: int = The number of tokens in the document
            chunks_count: int = The number of chunks the document was split into
        """

        response = requests.get(f"{self.base_url}/document", headers=self.headers)

        if response.status_code != 200:
            raise Exception(f'JUDINI: API Response was: {response.status_code}'
                            + f' {response.text} {JUDINI_TUTORIAL}')
        
        document_lists = response.json()
        return [Document(**document_dict) for document_dict in document_lists]
    
    def get_document(self, document_id: str) -> Document:
        """
        Retrieves a specific document from the CodeGPTPlus API.

        Parameters
        ----------
        document_id: The ID of the document to retrieve.

        Returns a json object representing the document with the following
        properties:
            id: str = The ID of the document
            user_id: str = The ID of the user who created the document
            name: str = The name of the document
            content: str = The content of the document
            file_type: str = The type of the document
            metadata: Optional[DocumentMetadata] = The metadata of the document
            tokens: int = The number of tokens in the document
            chunks_count: int = The number of chunks the document was split into
        """

        response = requests.get(f"{self.base_url}/document/{document_id}",
                                headers=self.headers)

        if response.status_code != 200:
           raise Exception(f'JUDINI: API Response was: {response.status_code}'
                            + f' {response.text} {JUDINI_TUTORIAL}')
        
        return Document(**response.json())
    
    def update_document_metadata(self,
                                 document_id: str,
                                 title: Optional[str] = None,
                                 description: Optional[str] = None,
                                 summary: Optional[str] = None,
                                 keywords: Optional[str] = None,
                                 language: Optional[str] = None):
        """
        Updates the metadata of a document in the CodeGPTPlus API.

        Parameters
        ----------
        document_id: The ID of the document to update.
        title: (optional) The updated title of the document.
        description: (optional) The updated description of the document.
        summary: (optional) The updated summary of the document.
        keywords: (optional) The updated keywords of the document.
        language: (optional) The updated language of the document.

        """
        document_metadata = (self.get_document(document_id).metadata or
                             DocumentMetadata())
        if title:
            document_metadata.title = title
        if description:
            document_metadata.description = description
        if summary:
            document_metadata.summary = summary
        if keywords:
            document_metadata.keywords = keywords
        if language:
            document_metadata.language = language

        payload = json.dumps(document_metadata.model_dump())

        response = requests.patch(f"{self.base_url}/document/{document_id}/metadata",
                                  headers=self.headers,
                                  data=payload)

        if response.status_code != 200:
            raise Exception(f'JUDINI: API Response was: {response.status_code}'
                            + f' {response.text} {JUDINI_TUTORIAL}')
        
        print("Document metadata updated successfully")
        return
    
    def _generate_document_metadata(self, file_path: str) -> DocumentMetadata:
        """
        Generates metadata for a document using the CodeGPTPlus API.

        Parameters
        ----------
        file_path: The path to the file to generate metadata for.

        Returns
        -------
        metadata: A DocumentMetadata object containing the metadata generated
        by the CodeGPTPlus API.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(f'JUDINI: File not found: {file_path}')
        
        file_type = mimetypes.guess_type(file_path)[0]
        
        headers = self.headers.copy()
        del headers['Content-Type']

        with open(file_path, 'rb') as file:
            file_tuple = (os.path.basename(file_path), file, file_type)
            response = requests.post(f"{self.base_url}/document/metadata",
                                     headers=headers,
                                     files={'file': file_tuple})
            
        if response.status_code != 200:
            raise Exception(f'JUDINI: API Response was: {response.status_code}'
                            + f' {response.text} {JUDINI_TUTORIAL}')
        
        return DocumentMetadata(**response.json()["metadata"])

    def upload_document(self, file_path: str,
                        generate_metadata: bool = False) -> Dict[str, str]:
        """
        Uploads a document to the CodeGPTPlus API.

        Parameters
        ----------
        file_path: The path to the file to upload.
        generate_metadata: (optional) Whether to extract metadata from the
                                      uploaded document.

        Returns
        -------
        response_json: A dictionary containing the document ID of the uploaded
                       document.
        """
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'JUDINI: File not found: {file_path}')
        
        file_type = mimetypes.guess_type(file_path)[0]
        
        headers = self.headers.copy()
        del headers['Content-Type']
        
        with open(file_path, 'rb') as file:
            file_tuple = (os.path.basename(file_path), file, file_type)
            response = requests.post(f"{self.base_url}/document",
                                     headers=headers,
                                     files={'file': file_tuple})
        
        if response.status_code != 200:
            raise Exception(f'JUDINI: API Response was: {response.status_code}'
                            + f' {response.text} {JUDINI_TUTORIAL}')
        
        document_id = response.json()['documentId']
        if generate_metadata:
            try:
                document_metadata = self._generate_document_metadata(file_path)
                self.update_document_metadata(document_id,
                                              **document_metadata.model_dump())
                return {'id' : document_id}
            except:
                print('Failed to generate document metadata.')
                return {'id' : document_id}

        return {'id' : document_id}
        
        
    def delete_document(self, document_id: str) -> None:
        """
        Deletes a document from the CodeGPTPlus API.

        Parameters
        ----------
        document_id: The ID of the document to delete.
        """

        response = requests.delete(f"{self.base_url}/document/{document_id}",
                                   headers=self.headers)
        
        if response.status_code != 200:
            raise Exception(f'JUDINI: API Response was: {response.status_code}'
                            + f' {response.text} {JUDINI_TUTORIAL}')
        
        print('Document deleted successfully')
        return