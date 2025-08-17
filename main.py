from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import openai
import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


load_dotenv()
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

app = FastAPI()

chat_history = [
    {"role": "system",
     "content": "You are a helpful assistant."}
]


class ChatRequest(BaseModel):
    message: str


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return FileResponse("static/index.html")


@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        chat_history.append({"role": "user", "content": request.message})

        response = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",
            messages=chat_history,
            max_tokens=100
        )

        reply = response['choices'][0]['message']['content'].strip()

        chat_history.append({"role": "assistant", "content": reply})

        return {"response": reply}
    except Exception as e:
        print("❌ OpenRouter error:", e)
        raise HTTPException(status_code=500, detail=str(e))
