import networkx as nx
import matplotlib.pyplot as plt
import json
import random

with open("clean_stations_distance.json") as f:
    data = json.load(f)

graph = nx.Graph()
positions = {
    "A01": [206, 1550, "Rose"],
    "A02": [325, 1550, "Rose"],
    "A03": [455, 1550, "Rose"],
    "A04": [570, 1550, "Rose"],
    "A05": [685, 1550, "Rose"],
    "A06": [832, 1550, "Rose"],
    "A07": [972, 1550, "Rose"],
    "A08": [1153, 1550, "Rose"],
    "A09": [1475, 1434, "Rose"],
    "A10": [1598, 1350, "Rose"],
    "A11": [1800, 1193, "Rose"],
    "A12": [1800, 1020, "Rose"],
    "A13": [1800, 950, "Rose"],
    "A14": [1800, 820, "Rose"],
    "A15": [1800, 725, "Rose"],
    "A16": [1800, 608, "Rose"],
    "A17": [1800, 490, "Rose"],
    "A18": [1908, 380, "Rose"],
    "A19": [1950, 325, "Rose"],
    "A20": [2009, 280, "Rose"],
}
# When getting pixel coords, need to subtact y coord from 1785 (height of image) to get correct coords (otherwise flipped)
for i in positions:
    positions[i][1] = 1785 - positions[i][1]
i = 0
for node, neighbors in data.items():
    # Only testing with A line nodes rn
    if "A" not in node:
        break
    graph.add_node(node, pos=(positions[node][0], positions[node][1]))
    for neighbor, weight in neighbors.items():
        # This right now is to just get the A line
        if "A" in neighbor:
            graph.add_edge(node, neighbor, weight=weight)
    i += 1
    # count += 1
    # if count == 5:
    #     break[]


nodes = graph.nodes(data=True)
print(nodes)
pos = {node: attr["pos"] for node, attr in nodes}
figure_size = (
    2560 / 80,
    1440 / 80,
)  # Convert pixels to inches by dividing by 80 (typical DPI)
plt.figure(figsize=figure_size)
nx.draw_networkx(graph, pos=pos, node_size=500, node_color="orange")
plt.show()
