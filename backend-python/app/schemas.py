from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Tuple

class HealthResponse(BaseModel):
    status: Literal["ok"] = "ok"
    version: str = "0.0.1"

class LatLon(BaseModel):
    lat: float
    lon: float

class RouteRequest(BaseModel):
    origin: LatLon = Field(..., description="Start point")
    destination: LatLon = Field(..., description="End point")
    preferences: Optional[dict] = None

class RouteResponse(BaseModel):
    length_m: float
    nodes: List[int]
    geometry: List[Tuple[float, float]]

    