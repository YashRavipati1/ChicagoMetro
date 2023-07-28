import networkx as nx

graph = nx.read_graphml("../datasets/tokyometro.graphml")

print(nx.dijkstra_path(graph, "A01", "G04", weight="weight"))
