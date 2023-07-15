"""
    This file defines the functionality for displaying any set of metro 
    stations given their longitude and latitude coordinates. To be run as a 
    script.
"""


# import libraries #
import networkx as nx
import matplotlib as plt
import json


# calculate coordinates #
# setup
BR_CORNER_COORD = (1000,  1000)     # using traditional pixel position as matrix
COORDS_PATH = './.json'
STATIONS_PATH = './secondary.json'

# execute setup
width = BR_CORNER_COORD[0]
height = BR_CORNER_COORD[1]

with open(COORDS_PATH, 'r') as f:
    coords_dict = json.load(f)
with open(STATIONS_PATH, 'r') as f:
    stations_dict = json.load(f)

# calculate positions
coords = dict()
for station_id, station_name in stations_dict.items():
    # check already calculated
    if station_name in coords:
        continue

    # calculate new coordinate
    coord = coords_dict[station_name]
    rel_pos = (coords[0] / width, coords[1] / height)
    coords[station_name] = rel_pos


# save results #
with open('pixel_positions.json', 'w') as f:
    json.dump(coords, f, indent=4)
