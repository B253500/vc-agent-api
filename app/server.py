from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from agents.market_sizing_agent import build_market_sizing_agent
from core.schemas import StartupProfile

app = FastAPI()

class MarketSizingRequest(BaseModel):
    name: Optional[str] = None
    sector: Optional[str] = None
    website: Optional[str] = None

@app.post("/market-sizing")
def market_sizing(data: MarketSizingRequest):
    # Build a partial profile
    profile = StartupProfile(
        name=data.name,
        sector=data.sector,
        website=data.website
    )

    # Run agent + chain
    _, task = build_market_sizing_agent(profile)
    task.execute_step()  # this will run the LLM with callback to update profile

    return {
        "TAM": profile.TAM or 0,
        "SAM": profile.SAM or 0,
        "SOM": profile.SOM or 0,
        "startup_name": profile.name,
        "sector": profile.sector,
        "source": "Market-sizing agent (AI)"
    }
