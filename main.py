import networkx as nx
import json


file_path = "/Users/noahantisseril/Desktop/Projects/MetroNavigator/clean_stations.json"
with open(file_path, "r") as file:
    data = json.load(file)

Graph = nx.Graph()

for stations in data:
    for key in data[stations]:
        Graph.add_edge(stations, key, weight=data[stations][key])
check = nx.shortest_path(Graph, "G01", "G19")
print(check)
print(nx.path_weight(Graph, path=check, weight="weight")/60)

