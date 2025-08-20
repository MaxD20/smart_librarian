from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.controllers.chat_controller import run_chat_with_tool

app = FastAPI()

class ChatRequest(BaseModel):
    query: str

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    response = run_chat_with_tool(request.query, return_as_string=True)  
    return {"reply": response}
