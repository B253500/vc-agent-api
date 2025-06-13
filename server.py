from fastapi import FastAPI
from pydantic import BaseModel
from agents.market_sizing_agent import build_market_sizing_agent
from core.schemas import StartupProfile

app = FastAPI()

class DeckInput(BaseModel):
    name: str | None = None
    sector: str | None = None
    website: str | None = None
    funding_stage: str | None = None

@app.post("/market-sizing")
async def market_sizing(input: DeckInput):
    profile = StartupProfile(**input.model_dump())
    agent, task = build_market_sizing_agent(profile)
    result = task.run()
    return {"result": result}
