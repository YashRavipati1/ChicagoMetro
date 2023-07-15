import networkx as nx
import matplotlib.pyplot as plt
import json
import random

with open("clean_stations.json") as f:
    data = json.load(f)

with open("secondary.json", "r") as file:
    names = json.load(file)

graph = nx.Graph()
positions = {
    "A01": [206, 1550, "Red"],
    "A02": [325, 1550, "Red"],
    "A03": [455, 1550, "Red"],
    "A04": [570, 1550, "Red"],
    "A05": [685, 1550, "Red"],
    "A06": [832, 1550, "Red"],
    "A07": [972, 1550, "Red"],
    "A08": [1153, 1550, "Red"],
    "A09": [1475, 1434, "Red"],
    "A10": [1598, 1350, "Red"],
    "A11": [1800, 1193, "Red"],
    "A12": [1800, 1020, "Red"],
    "A13": [1800, 950, "Red"],
    "A14": [1800, 820, "Red"],
    "A15": [1800, 725, "Red"],
    "A16": [1800, 608, "Red"],
    "A17": [1800, 490, "Red"],
    "A18": [1908, 380, "Red"],
    "A19": [1950, 325, "Red"],
    "A20": [2009, 280, "Red"],
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
    "I01": [574, 1425, "Blue"],
    "I02": [730, 1425, "Blue"],
    "I03": [890, 1425, "Blue"],
    "I04": [1153, 1550, "Blue"],
    "I05": [1321, 1490, "Blue"],
    "I06": [1432, 1379, "Blue"],
    "I07": [1498, 1291, "Blue"],
    "I08": [1526, 1185, "Blue"],
    "I09": [1397, 941, "Blue"],
    "I10": [1270, 725, "Blue"],
    "I11": [1270, 615, "Blue"],
    "I12": [1201, 488, "Blue"],
    "I13": [1104, 391, "Blue"],
    "I14": [1054, 338, "Blue"],
    "I15": [1004, 280, "Blue"],
    "I16": [923, 236, "Blue"],
    "I17": [772, 236, "Blue"],
    "I18": [708, 236, "Blue"],
    "I19": [641, 206, "Blue"],
    "I20": [591, 157, "Blue"],
    "I21": [548, 112, "Blue"],
    "I22": [474, 61, "Blue"],
    "I23": [413, 61, "Blue"],
    "I24": [350, 61, "Blue"],
    "I25": [290, 61, "Blue"],
    "I26": [230, 61, "Blue"],
    "I27": [170, 61, "Blue"],
}
# When getting pixel coords, need to subtact y coord from 1785 (height of image) to get correct coords (otherwise flipped)
for i in positions:
    positions[i][1] = 1785 - positions[i][1]

for node, neighbors in data.items():
    if "A" not in node and "C" not in node and "Y" not in node and "I" not in node:
        continue
    graph.add_node(node, pos=(positions[node][0], positions[node][1]))
    for neighbor, weight in neighbors.items():
        if "A" in neighbor or "C" in neighbor or "Y" in neighbor or "I" in neighbor:
            graph.add_edge(node, neighbor, weight=weight)

nodes = graph.nodes(data=True)
edges = graph.edges(data=True)
path = ["A01", "A02", "A03"]
color_map_nodes = []
color_map_edges = []
for edge in edges:
    if edge[0] and edge[1] in path:
        color_map_edges.append("orange")
    else:
        color_map_edges.append("0.5")
for node in graph:
    if node in path:
        color_map_nodes.append("orange")
    else:
        color_map_nodes.append("0.5")
pos = {node: attr["pos"] for node, attr in nodes}
names = {key: value for key, value in names.items() if key in nodes and key in path}
nx.draw_networkx(
    graph,
    pos=pos,
    node_size=50,
    labels=names,
    node_color=color_map_nodes,
    edge_color=color_map_edges,
    with_labels=True,
    font_size=8,
)
plt.show()
