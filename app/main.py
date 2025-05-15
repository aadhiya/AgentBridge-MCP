from fastapi import FastAPI
from pydantic import BaseModel
from app.router import dispatch_task

app = FastAPI()

class MCPRequest(BaseModel):
    task: str
    payload: dict

@app.post("/mcp")
def mcp_handler(req: MCPRequest):
    return dispatch_task(req.task, req.payload)
