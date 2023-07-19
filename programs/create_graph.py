import json
import networkx as nx
import matplotlib.pyplot as plt

with open("../datasets/clean_stations_distance.json") as f:
    data = json.load(f)

graph = nx.Graph()

color_maps = {
    "BASE": "0.5",
    "A": "Blue",
    "I": "Lime",
    "S": "Magenta",
    "E": "Orange",
    "G": "Red",
    "M": "Silver",
    "H": "Skyblue",
    "T": "Green",
    "C": "Gold",
    "Y": "Purple",
    "Z": "Darkgreen",
    "N": "Brown",
    "F": "Yellow",
}

for node, neighbors in data.items():
    graph.add_node(node, color=color_maps["BASE"])
    for neighbor, weight in neighbors.items():
        graph.add_edge(node, neighbor, weight=weight, color=color_maps["BASE"])
    # count += 1
    # if count == 5:
    #     break

nx.write_graphml(graph, "../datasets/tokyometro.graphml")


pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(graph, "weight")
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
plt.show()
