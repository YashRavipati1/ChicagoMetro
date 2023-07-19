"""
    Hosting for the web app.
"""


# ----------------- imports ----------------- #
from flask import Flask             # routing
from algorithm import *             # path-finding
from map_visualizer import *        # visualizing
import networkx as nx               # graph


# ----------------- routes ----------------- #
app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_path(source, destination):
    # load graph #
    metro_graph = nx.read_graphml("../datasets/tokyometro.graphml")

    # find path #
    distance, path, path_string = path_find(metro_graph, source, destination)

    # get visualization #
    visualize_path(path)

    # user output #




data, names, positions, station_lookup = load_data()
metro = load_graph(data, positions)
grr = path_find(metro, "A01", "S21")[1]
print(grr)
visualize_path(grr)