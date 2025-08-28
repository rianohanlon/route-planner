from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import routes
from app.services.graph import ensure_graph_loaded

app = FastAPI(title="Route Planner API", version="0.0.1", docs_url="/docs", redoc_url="/redoc")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)

@app.on_event("startup")
async def maybe_preload():
    if settings.preload_graph:
        ensure_graph_loaded()