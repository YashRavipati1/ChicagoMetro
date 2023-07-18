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
    distance, path, path_string = dijkstra(metro_graph, source, destination)

    # get visualization #
    visualize_path(path)

    # user output #
    


