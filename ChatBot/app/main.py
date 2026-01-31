import os
from fastapi import FastAPI
from pydantic import BaseModel
from app.gemini.gemini import GeminiClient

# ----------------------------
# Models
# ----------------------------

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str

# ----------------------------
# App setup
# ----------------------------

app = FastAPI()

gemini = GeminiClient(api_key=os.getenv("GOOGLE_API_KEY"))

@app.get("/")
async def root():
    return {"message": "Chatbot is running"}

def load_system_prompt():
    try:
        with open("system_prompt.md", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ' none '

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    system_prompt = load_system_prompt()

    reply = await gemini.chat(system_prompt, request.prompt)

    return {"response": reply}

