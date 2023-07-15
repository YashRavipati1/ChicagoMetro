"""
    This file defines the functionality for displaying any set of metro 
    stations given their longitude and latitude coordinates. To be run as a 
    script.
"""


# import libraries #
import networkx as nx
import matplotlib as plt
import json
import * from dijkstras.py


# calculate coordinates #
# setup
BR_CORNER_COORD = (2526,  1785)     # using traditional pixel position as matrix
COORDS_PATH = './pixels.json'
STATIONS_PATH = './secondary.json'
SCALE = 1

# execute setup
width = BR_CORNER_COORD[0]
height = BR_CORNER_COORD[1]

with open(COORDS_PATH, 'r') as f:
    coords = json.load(f)
with open(STATIONS_PATH, 'r') as f:
    stations_dict = json.load(f)

# # calculate positions
# coords = dict()
# for station_id, station_name in stations_dict.items():
#     # check already calculated
#     if station_name in coords:
#         continue

#     # calculate new coordinate
#     coord = coords_dict[station_name]
#     rel_pos = (coords[0] / width, coords[1] / height)
#     coords[station_name] = rel_pos


# save results #
with open('pixel_positions.json', 'w') as f:
    json.dump(coords, f, indent=4)


# show metro map #
# scale relative positions
coords = {k: v * SCALE for k, v in coords.items()}

# get path
path = dijkstras()

edge_colors = nx.get_edge_attributes(graph, 'color').values()
node_colors = nx.get_node_attributes(graph, 'color').values()
widths = nx.get_edge_attributes(graph, 'weight')

nx.draw_networkx(
    graph,
    pos=pos,
    node_size=50,
    # width=widths,
    node_color=node_colors,
    edge_color=edge_colors,
    with_labels=True
)
# nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
plt.show()
