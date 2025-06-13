from pydantic import BaseModel
from typing import Optional

class StartupProfile(BaseModel):
    name: Optional[str] = None
    sector: Optional[str] = None
    website: Optional[str] = None
    funding_stage: Optional[str] = None
    TAM: Optional[float] = None
    SAM: Optional[float] = None
    SOM: Optional[float] = None
