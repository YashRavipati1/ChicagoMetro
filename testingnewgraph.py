import networkx as nx
import matplotlib.pyplot as plt
import json
import random

with open("clean_stations_distance.json") as f:
    data = json.load(f)

with open("secondary.json", "r") as file:
    names = json.load(file)

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
    "C01": [365, 1110, "Green"],
    "C02": [408, 1110, "Green"],
    "C03": [620, 1110, "Green"],
    "C04": [823, 1230, "Green"],
    "C05": [915, 1230, "Green"],
    "C06": [1037, 1230, "Green"],
    "C07": [1225, 1230, "Green"],
    "C08": [1360, 1230, "Green"],
    "C09": [1526, 1185, "Green"],
    "C10": [1397, 1010, "Green"],
    "C11": [1397, 941, "Green"],
    "C12": [1397, 725, "Green"],
    "C13": [1397, 525, "Green"],
    "C14": [1397, 420, "Green"],
    "C15": [1397, 335, "Green"],
    "C16": [1397, 230, "Green"],
    "C17": [1550, 120, "Green"],
    "C18": [1910, 120, "Green"],
    "C19": [2092, 120, "Green"],
    "C20": [2160, 72, "Green"],
    "Y01": [108, 220, "Gold"],
    "Y02": [178, 220, "Gold"],
    "Y03": [251, 220, "Gold"],
    "Y04": [316, 220, "Gold"],
    "Y05": [389, 220, "Gold"],
    "Y06": [458, 235, "Gold"],
    "Y07": [525, 304, "Gold"],
    "Y08": [591, 367, "Gold"],
    "Y09": [660, 419, "Gold"],
    "Y10": [754, 486, "Gold"],
    "Y11": [879, 486, "Gold"],
    "Y12": [991, 516, "Gold"],
    "Y13": [1129, 667, "Gold"],
    "Y14": [1022, 784, "Gold"],
    "Y15": [1048, 900, "Gold"],
    "Y16": [1143, 992, "Gold"],
    "Y17": [1341, 1129, "Gold"],
    "Y18": [1594, 1129, "Gold"],
    "Y19": [1700, 1129, "Gold"],
    "Y20": [1832, 1129, "Gold"],
    "Y21": [2001, 1129, "Gold"],
    "Y22": [2100, 1129, "Gold"],
    "Y23": [2195, 1129, "Gold"],
    "Y24": [2300, 1129, "Gold"],
}
# When getting pixel coords, need to subtact y coord from 1785 (height of image) to get correct coords (otherwise flipped)
for i in positions:
    positions[i][1] = 1785 - positions[i][1]

for node, neighbors in data.items():
    if "A" not in node and "C" not in node and "Y" not in node:
        continue
    graph.add_node(node, pos=(positions[node][0], positions[node][1]))
    for neighbor, weight in neighbors.items():
        if "A" in neighbor or "C" in neighbor or "Y" in neighbor:
            graph.add_edge(node, neighbor, weight=weight)

graph = nx.relabel_nodes(graph, names)
nodes = graph.nodes(data=True)
print(nodes)
pos = {node: attr["pos"] for node, attr in nodes}
nx.draw_networkx(graph, pos=pos, node_size=500, node_color="orange")
plt.show()
