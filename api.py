from fastapi import FastAPI
from pydantic import BaseModel
from services.llm_service import get_debug_response

app = FastAPI()

class DebugRequest(BaseModel):
    error: str

@app.get("/")
def home():
    return {"message": "AI Java Debugger API is running"}

@app.post("/debug")
def debug_error(request: DebugRequest):
    response = get_debug_response(request.error)
    return response
