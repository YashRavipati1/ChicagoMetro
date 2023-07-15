import networkx as nx
import matplotlib.pyplot as plt
import json
import random

with open("clean_stations_distance.json") as f:
    data = json.load(f)

graph = nx.Graph()
x = [random.randint(1, 1000) for _ in range(len(data))]
y = [random.randint(1, 1000) for _ in range(len(data))]
i = 0
for node, neighbors in data.items():
    graph.add_node(node, pos=(x[i], y[i]))
    for neighbor, weight in neighbors.items():
        graph.add_edge(node, neighbor, weight=weight)
    i += 1
    # count += 1
    # if count == 5:
    #     break[]


nodes = graph.nodes(data=True)
print(nodes)
pos = {node: attr["pos"] for node, attr in nodes}
nx.draw_networkx(graph, pos=pos, node_size=500, node_color="orange")
plt.show()
