from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class MarketSizingRequest(BaseModel):
    name: Optional[str] = None
    sector: Optional[str] = None
    website: Optional[str] = None

@app.post("/market-sizing")
def market_sizing(data: MarketSizingRequest):
    # Simple mock response — replace with real CrewAI agent logic
    return {
        "TAM": 4500,
        "SAM": 1200,
        "SOM": 300,
        "startup_name": data.name,
        "sector": data.sector,
        "source": "Market-sizing agent (mock)"
    }
