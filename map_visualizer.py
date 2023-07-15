"""
    This file defines the functionality for displaying any set of metro 
    stations given their longitude and latitude coordinates.
"""


# import libraries #
import networkx as nx
import matplotlib as plt


# calculate coordinates #
# setup
TL_CORNER_COORD = (-1,  -1)
BR_CORNER_COORD = (-1,  -1)
COORDS_PATH = './.json'
STATIONS_PATH = './secondary.json'

# execute setup
wstart = TL_CORNER_COORD[0]
hstart = BR_CORNER_COORD[1]
width = BR_CORNER_COORD[0] - wstart
height = TL_CORNER_COORD[1] - hstart

with open(COORDS_PATH) as f:
    coords_dict = json.load(f)
with open(STATIONS_PATH) as f:
    stations_dict = json.load(f)

# calculate positions
coords = dict()

for station_id, station_name in stations_dict.items():
    # calculate new coordinate
    coord = 

