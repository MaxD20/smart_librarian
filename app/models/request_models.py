from pydantic import BaseModel

class ChatRequest(BaseModel):
    query: str

class ImageRequest(BaseModel):
    title: str