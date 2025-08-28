from typing import Tuple, Dict, Any
import osmnx as ox
import networkx as nx
from app.config import settings

_GRAPH: Dict[str, Any] = {"G_m": None, "G_wgs": None}

def ensure_graph_loaded():
    if _GRAPH["G_m"] is not None:
        return
    ox.settings.use_cache = settings.osmnx_cache
    G_wgs = ox.graph_from_place(settings.graph_place, network_type=settings.graph_network_type)
    G_m = ox.project_graph(G_wgs)
    G_m = ox.add_edge_lengths(G_m)
    _GRAPH["G_m"] = G_m
    _GRAPH["G_wgs"] = ox.project_graph(G_m, to_crs="EPSG:4326")

def get_shortest_path(origin: Tuple[float, float], destination: Tuple[float, float]):

    if _GRAPH[G_m] is None:
        ensure_graph_loaded()
    G_m = _GRAPH["G_m"]
    G_wgs = _GRAPH["G_wgs"]

    src = ox.distance.nearest_nodes(G_wgs, origin[1], origin[0])
    dst = ox.distance.nearest_nodes(G_wgs, destination[1], destination[0])

    nodes_gdf = ox.graph_to_gdfs(G_wgs, edges=False)
    coords = [(float(nodes_gdf.loc[n].y), float(nodes_gdf.loc[n].x)) for n in path]
    return {"length_m": float(length_m), "nodes": [int(n) for n in path], "geometry": coords}
