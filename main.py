from fastapi import FastAPI
from app.routers import chat

app = FastAPI()

app.include_router(chat.router)

@app.get("/")
def read_root():
    return {"message": "AutoSupportAI Backend is running"}
