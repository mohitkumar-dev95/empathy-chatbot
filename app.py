import socket
import json
from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import generate_response

app = FastAPI(title="Empathy Analyzer API")

# --- ELK LOGGING CONFIG ---
LOGSTASH_IP = "100.128.162.10"
LOGSTASH_PORT = 5000

def send_to_elk(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((LOGSTASH_IP, LOGSTASH_PORT))
            s.sendall((json.dumps({"message": message}) + "\n").encode())
    except:
        pass # Ignore if ELK is down so the app doesn't crash
# --------------------------

class ChatRequest(BaseModel):
    text: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    bot_response = generate_response(request.text)
    
    # SEND LOG TO ELK
    send_to_elk(f"USER: {request.text} | BOT: {bot_response}")
    
    return ChatResponse(response=bot_response)

@app.get("/")
async def root():
    send_to_elk("Root endpoint accessed")
    return {"message": "Empathy Analyzer API is running...Send POST requests to /chat"}
