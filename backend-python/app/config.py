from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    cors_allow_origins: List[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]
    preload_graph: bool = False
    graph_place: str = "Seattle, Washington, USA"
    graph_network_type: str = "walk"
    osmnx_cache: bool = True
    model_config = SettingsConfigDict(ev_file=".env", env_file_encoding="utf-8")

settings = Settings()
