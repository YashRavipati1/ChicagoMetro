# ----------- libraries import ----------- #
import networkx as nx
import matplotlib.pyplot as plt
import json
from dijkstras import *


# ----------- load files ----------- #
with open("clean_stations.json") as f:
    data = json.load(f)

with open("secondary.json", "r") as f:
    names = json.load(f)

graph = nx.Graph()
with open("station_positions.json", "r") as f:
    positions = json.load(f)

Emerald = "#00ad9b"
Leaf = "#7ab728"
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
    "E01": [543, 824, "Magenta"],
    "E02": [650, 715, "Magenta"],
    "E03": [783, 676, "Magenta"],
    "E04": [875, 676, "Magenta"],
    "E05": [964, 676, "Magenta"],
    "E06": [1129, 667, "Magenta"],
    "E07": [1201, 490, "Magenta"],
    "E08": [1321, 490, "Magenta"],
    "E09": [1563, 490, "Magenta"],
    "E10": [1712, 490, "Magenta"],
    "E11": [1800, 490, "Magenta"],
    "E12": [1962, 589, "Magenta"],
    "E13": [1998, 726, "Magenta"],
    "E14": [1998, 822, "Magenta"],
    "E15": [2013, 952, "Magenta"],
    "E16": [2001, 1129, "Magenta"],
    "E17": [1949, 1259, "Magenta"],
    "E18": [1868, 1346, "Magenta"],
    "E19": [1624, 1432, "Magenta"],
    "E20": [1475, 1434, "Magenta"],
    "E21": [1218, 1429, "Magenta"],
    "E22": [1059, 1429, "Magenta"],
    "E23": [955, 1320, "Magenta"],
    "E24": [901, 1042, "Magenta"],
    "E25": [742, 1011, "Magenta"],
    "E26": [576, 1013, "Magenta"],
    "E27": [543, 824, "Magenta"],
    "E28": [467, 883, "Magenta"],
    "E29": [394, 886, "Magenta"],
    "E30": [394, 822, "Magenta"],
    "E31": [392, 680, "Magenta"],
    "E32": [362, 548, "Magenta"],
    "E33": [305, 507, "Magenta"],
    "E34": [269, 471, "Magenta"],
    "E35": [222, 423, "Magenta"],
    "E36": [170, 379, "Magenta"],
    "E37": [130, 335, "Magenta"],
    "E38": [93, 299, "Magenta"],
    "G01": [634, 1220, "Orange"],
    "G02": [823, 1230, "Orange"],
    "G03": [891, 1113, "Orange"],
    "G04": [901, 1042, "Orange"],
    "G05": [1143, 992, "Orange"],
    "G06": [1225, 1230, "Orange"],
    "G07": [1300, 1335, "Orange"],
    "G08": [1598, 1350, "Orange"],
    "G09": [1700, 1129, "Orange"],
    "G10": [1734, 1022, "Orange"],
    "G11": [1800, 950, "Orange"],
    "G12": [1655, 874, "Orange"],
    "G13": [1581, 774, "Orange"],
    "G14": [1572, 597, "Orange"],
    "G15": [1563, 489, "Orange"],
    "G16": [1580, 376, "Orange"],
    "G17": [1701, 379, "Orange"],
    "G18": [1778, 378, "Orange"],
    "G19": [1908, 380, "Orange"],
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
    "Y18": [1598, 1128, "Gold"],
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
    "Mb03": [84, 820, "Red"],
    "Mb04": [171, 820, "Red"],
    "Mb05": [264, 821, "Red"],
    "M01": [143, 591, "Red"],
    "M02": [185, 643, "Red"],
    "M03": [222, 682, "Red"],
    "M04": [263, 725, "Red"],
    "M05": [307, 766, "Red"],
    "M06": [394, 822, "Red"],
    "M07": [471, 820, "Red"],
    "M08": [543, 824, "Red"],
    "M09": [739, 889, "Red"],
    "M10": [812, 887, "Red"],
    "M11": [871, 886, "Red"],
    "M12": [946, 889, "Red"],
    "M13": [1143, 992, "Red"],
    "M14": [1225, 1230, "Red"],
    "M15": [1360, 1230, "Red"],
    "M16": [1700, 1129, "Red"],
    "M17": [1595, 1036, "Red"],
    "M18": [1397, 941, "Red"],
    "M19": [1397, 725, "Red"],
    "M20": [1446, 619, "Red"],
    "M21": [1321, 490, "Red"],
    "M22": [1201, 488, "Red"],
    "M23": [989, 421, "Red"],
    "M24": [873, 420, "Red"],
    "M25": [660, 419, "Red"],
    "T01": [274, 590, "Skyblue"],
    "T02": [442, 590, "Skyblue"],
    "T03": [589, 590, "Skyblue"],
    "T04": [820, 590, "Skyblue"],
    "T05": [935, 590, "Skyblue"],
    "T06": [1129, 667, "Skyblue"],
    "T07": [1253, 844, "Skyblue"],
    "T08": [1305, 904, "Skyblue"],
    "T09": [1397, 941, "Skyblue"],
    "T10": [1800, 950, "Skyblue"],
    "T11": [1906, 952, "Skyblue"],
    "T12": [2013, 952, "Skyblue"],
    "T13": [2018, 952, "Skyblue"],
    "T14": [2112, 917, "Skyblue"],
    "T15": [2141, 887, "Skyblue"],
    "T16": [2176, 854, "Skyblue"],
    "T17": [2206, 825, "Skyblue"],
    "T18": [2240, 795, "Skyblue"],
    "T19": [2273, 764, "Skyblue"],
    "T20": [2303, 724, "Skyblue"],
    "T21": [2338, 695, "Skyblue"],
    "T22": [2367, 661, "Skyblue"],
    "T23": [2407, 612, "Skyblue"],
    "Z01": [634, 1220, "Purple"],
    "Z02": [823, 1230, "Purple"],
    "Z03": [901, 1042, "Purple"],
    "Z04": [1143, 992, "Purple"],
    "Z05": [1213, 923, "Purple"],
    "Z06": [1253, 844, "Purple"],
    "Z07": [1270, 725, "Purple"],
    "Z08": [1397, 941, "Purple"],
    "Z09": [1655, 874, "Purple"],
    "Z10": [1936, 874, "Purple"],
    "Z11": [1998, 822, "Purple"],
    "Z12": [2094, 618, "Purple"],
    "Z13": [2094, 453, "Purple"],
    "Z14": [2009, 280, "Purple"],
    "N01": [574, 1425, Emerald],
    "N02": [730, 1425, Emerald],
    "N03": [890, 1425, Emerald],
    "N04": [1059, 1429, Emerald],
    "N05": [1148, 1290, Emerald],
    "N06": [1225, 1230, Emerald],
    "N07": [1143, 992, Emerald],
    "N08": [946, 889, Emerald],
    "N09": [1022, 784, Emerald],
    "N10": [1129, 667, Emerald],
    "N11": [1201, 490, Emerald],
    "N12": [1166, 404, Emerald],
    "N13": [1166, 350, Emerald],
    "N14": [1166, 282, Emerald],
    "N15": [1166, 220, Emerald],
    "N16": [1130, 167, Emerald],
    "N17": [1054, 111, Emerald],
    "N18": [986, 111, Emerald],
    "N19": [901, 111, Emerald],
    "S01": [543, 824, Leaf],
    "S02": [739, 889, Leaf],
    "S03": [870, 784, Leaf],
    "S04": [1022, 784, Leaf],
    "S05": [1253, 844, Leaf],
    "S06": [1270, 725, Leaf],
    "S07": [1397, 725, Leaf],
    "S08": [1655, 725, Leaf],
    "S09": [1800, 725, Leaf],
    "S10": [1899, 725, Leaf],
    "S11": [1998, 726, Leaf],
    "S12": [2053, 685, Leaf],
    "S13": [2094, 618, Leaf],
    "S14": [2167, 572, Leaf],
    "S15": [2199, 539, Leaf],
    "S16": [2231, 503, Leaf],
    "S17": [2264, 469, Leaf],
    "S18": [2296, 441, Leaf],
    "S19": [2328, 410, Leaf],
    "S20": [2358, 381, Leaf],
    "S21": [2358, 321, Leaf],
}

# When getting pixel coords, need to subtact y coord from 1785 (height of image) to get correct coords (otherwise flipped)
for i in positions:
    positions[i][1] = 1785 - positions[i][1]

added_lines = ["A", "C", "Y", "I", "T", "E", "G", "Z", "M", "N", "S"]
for node, neighbors in data.items():
    if all(char not in node for char in added_lines):
        continue
    graph.add_node(node, pos=(positions[node][0], positions[node][1]))
    for neighbor, weight in neighbors.items():
        if any(char in neighbor for char in added_lines):
            graph.add_edge(node, neighbor, weight=weight)


# ----------- find path ----------- #
# get path #
# path = ["A01", "A02", "A03"]
path = dijkstra(graph, "A01", "M25")[1]


# convert to station names #
# load stations lookup
with open("full_intersections.json", "r") as f:
    station_lookup = json.load(f)

# modify lookup to congregate names
station_lookup = {k: list(v.keys()) for k, v in station_lookup.items()}
# replace
path_expanded = []
previous_station = None
for station in path:
    # get associated stations
    station_name = names[station]
    if station_name == previous_station:
        continue

    intersecting_stations = station_lookup[station_name]
    previous_station = station_name

    # add
    path_expanded += intersecting_stations
# ----------- draw map ----------- #
# get attributes #
nodes = graph.nodes(data=True)
edges = graph.edges(data=True)
color_map_nodes = ["0.5"] * len(nodes)
color_map_edges = ["0.5"] * len(edges)

# edge colors for only path
for i, edge in enumerate(edges):
    if edge[0] and edge[1] in path:
        color_map_edges[i] = positions[edge[0]][2]

# labels
names = {key: value for key, value in names.items() if key in nodes and key in path}

nodes_list = list(graph.nodes())
# node colors for only path
for i, node in enumerate(graph):
    if node in path:
        color_map_nodes[i] = positions[node][2]
        station_name = names[node]
        intersecting_stations = station_lookup[station_name]
        if node == "I08":
            print(intersecting_stations)
        for station in intersecting_stations:
            color_map_nodes[nodes_list.index(station)] = positions[node][2]

# positions
# pos = {node: attr["pos"] for node, attr in nodes}
pos = nx.get_node_attributes(graph, "pos")
print(path)
# draw graph #
nx.draw_networkx(
    graph,
    pos=pos,
    node_size=50,
    labels=names,
    node_color=color_map_nodes,
    edge_color=color_map_edges,
    with_labels=False,
    font_size=8,
)

# show metro map #
# edge_colors = nx.get_edge_attributes(graph, 'color').values()
# node_colors = nx.get_node_attributes(graph, 'color').values()

# nx.draw_networkx(
#     graph,
#     pos=pos,
#     node_size=50,
#     # width=widths,
#     node_color=node_colors,
#     edge_color=edge_colors,
#     with_labels=True
# )

plt.show()
