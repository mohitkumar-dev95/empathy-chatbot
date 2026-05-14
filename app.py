from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import generate_response

app = FastAPI(title="Empathy Analyzer API")

class ChatRequest(BaseModel):
    text: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    bot_response = generate_response(request.text)
    return ChatResponse(response=bot_response)

@app.get("/")
async def root():
    return {"message": "Empathy Analyzer API is running. Send POST requests to /chat"}
