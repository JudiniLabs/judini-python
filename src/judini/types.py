from pydantic import BaseModel, field_validator
from typing import Optional, List
import json

class Agent(BaseModel):
    id: str
    """The ID of the agent"""
    name: str
    """The name of the agent"""
    prompt: str
    """The prompt of the agent"""
    model: str
    """The model of the agent"""
    agent_documents: Optional[List[str]] = None
    """The list of documents associated with the agent"""
    welcome: str
    """The welcome message of the agent"""
    pincode: Optional[str] = None
    """The pincode of the agent"""
    is_public: bool
    """Whether the agent is public or not"""
    agent_type: str
    """The type of the agent"""

class DocumentMetadata(BaseModel):
    title: Optional[str] = ""
    """The title of the document"""
    description: Optional[str] = ""
    """The description of the document"""
    summary: Optional[str] = ""
    """The summary of the document"""
    keywords: Optional[str] = ""
    """The keywords of the document, separated by commas"""
    language: Optional[str] = ""
    """The language of the document"""


class Document(BaseModel):
    id: str
    """The ID of the document"""
    user_id: str
    """The ID of the user who created the document"""
    name: str
    """The name of the document"""
    file_type: str
    """The type of the document"""
    metadata: Optional[DocumentMetadata] = None
    """The metadata of the document"""
    tokens: int
    """The number of tokens in the document"""
    chunks_count: Optional[int] = None
    """The number of chunks the document was split into"""
    content: Optional[str] = None
    """The content of the document"""

    @field_validator("metadata", mode="before")
    def json_loads(cls, v):
        if v:
            if isinstance(v, str):
                return json.loads(v)
            else:
                return v