Sprint 1 Scope:

Local web-app with a map of the seattle metro. OSM basemap displayed. Network of public, walkable edges. 

Data: OSM via OSMnx filtered to be public walkable edges only.
Routing Engine: Graph built using NetworkX MultiDiGraph using Dijkstra to start, then find an alternative path back. Graph must be pre-built and loaded into memory.
