from fastapi import APIRouter, HTTPException
from app.schemas import HealthResponse, RouteRequest, RouteResponse
from app.services.graph import get_shortest_path

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse()

@router.post("/route", response_model=RouteResponse)
def route(req: RouteRequest):
    try:
        result = get_shortest_path(
            origin=(req,origin.lat, req.origin.lon),
            destination=(req.destination.lat, req.destination.lon)
        )
        return RouteResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Routing Error")
    
