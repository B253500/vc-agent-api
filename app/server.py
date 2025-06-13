from app.pdf_generator import router as pdf_router
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from agents.market_sizing_agent import build_market_sizing_agent
from core.schemas import StartupProfile

app = FastAPI()

app.include_router(pdf_router)

class MarketSizingRequest(BaseModel):
    name: Optional[str] = None
    sector: Optional[str] = None
    website: Optional[str] = None

@app.post("/market-sizing")
def market_sizing(data: MarketSizingRequest):
    profile = StartupProfile(
        name=data.name,
        sector=data.sector,
        website=data.website
    )

    try:
        # Build agent and run task
        _, task = build_market_sizing_agent(profile)
        task.execute_step()
    except Exception as e:
        # For debugging — log and return friendly error
        return {
            "error": "Agent execution failed",
            "details": str(e),
            "startup_name": profile.name,
            "sector": profile.sector
        }

    return {
        "TAM": profile.TAM or 0,
        "SAM": profile.SAM or 0,
        "SOM": profile.SOM or 0,
        "startup_name": profile.name,
        "sector": profile.sector,
        "source": "Market-sizing agent (AI)"
    }
