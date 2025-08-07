from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import openai
import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

app = FastAPI()

class ChatRequest(BaseModel):
    message: str


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return FileResponse("static/index.html")



@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": req.message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return {"response": reply.strip()}
    except Exception as e:
        print("❌ OpenRouter error:", e)
        raise HTTPException(status_code=500, detail=str(e))
