import json
import networkx as nx
import matplotlib.pyplot as plt

with open("clean_stations_distance.json") as f:
    data = json.load(f)

graph = nx.Graph()

for node, neighbors in data.items():
    graph.add_node(node)
    for neighbor, weight in neighbors.items():
        graph.add_edge(node, neighbor, weight=weight)
    # count += 1
    # if count == 5:
    #     break

nx.write_graphml(graph, "tokyometro.graphml")


pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(graph, "weight")
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
plt.show()
