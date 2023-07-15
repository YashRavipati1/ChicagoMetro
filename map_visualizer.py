"""
    This file defines the functionality for displaying any set of metro 
    stations given their longitude and latitude coordinates. To be run as a 
    script.
"""


# import libraries #
import networkx as nx
import matplotlib as plt
import json
# import * from dijkstras.py


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
    coords_dict = json.load(f)
with open(STATIONS_PATH, 'r') as f:
    stations_dict = json.load(f)

# calculate positions
coords = dict()     # stores station name : position
for station_id, station_name in stations_dict.items():
    # check already calculated
    station_name = station_name.title()
    try:
        coords_dict[station_id]
    except:
        continue
        
    if station_name in coords:
        print(station_name, station_id)
        coords[station_name][station_id] = list(coords[station_name].values())[0]
        print(coords[station_name])
    else:
        coords[station_name] = dict()
        coords[station_name][station_id] = coords_dict[station_id]

# convert back
combined_coords = dict()
for stations in coords.values():
    combined_coords.update(stations)

    # # calculate new coordinate
    # coord = coords_dict[station_name]
    # rel_pos = (coords[0] / width, coords[1] / height)
    # coords[station_name] = rel_pos


# save results #
with open('intersections_pixels.json', 'w') as f:
    json.dump(combined_coords, f, indent=4)
with open('temp_results.json', 'w') as f:
    json.dump(coords, f, indent=4)


# # show metro map #
# # scale relative positions
# coords = {k: v * SCALE for k, v in coords.items()}

# # get path
# path = dijkstras()

# edge_colors = nx.get_edge_attributes(graph, 'color').values()
# node_colors = nx.get_node_attributes(graph, 'color').values()
# widths = nx.get_edge_attributes(graph, 'weight')

# nx.draw_networkx(
#     graph,
#     pos=pos,
#     node_size=50,
#     # width=widths,
#     node_color=node_colors,
#     edge_color=edge_colors,
#     with_labels=True
# )
# # nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
# plt.show()
