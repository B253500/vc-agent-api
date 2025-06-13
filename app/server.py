from fastapi import FastAPI
from pydantic import BaseModel
from agents.market_sizing_agent import build_market_sizing_agent
from core.schemas import StartupProfile

app = FastAPI()

class ProfileRequest(BaseModel):
    profile: StartupProfile

@app.post("/agent/market")
async def run_market_agent(req: ProfileRequest):
    agent, task = build_market_sizing_agent(req.profile)
    result = task.callback()
    return {"response": result}
