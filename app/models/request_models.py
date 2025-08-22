from pydantic import BaseModel


class ChatRequest(BaseModel):
    query: str


class ImageRequest(BaseModel):
    title: str
    request_id: str | None = None


class ListenRequest(BaseModel):
    request_id: str | None = None
    text: str
