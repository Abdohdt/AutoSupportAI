from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
def chat_endpoint(message: str):
    # Placeholder for LLM logic
    return {"response": f"You said: {message}"}