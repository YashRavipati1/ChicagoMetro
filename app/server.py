"""
    Hosting for the web app.
"""


# ----------------- imports ----------------- #
from flask import Flask, jsonify  # routing
from algorithm import *  # path-finding
from map_visualizer import *  # visualizing
import networkx as nx  # graph
from flask_cors import CORS


# ----------------- routes ----------------- #
app = Flask(__name__)
CORS(app)


@app.route("/calculate_path/<source>/<destination>", methods=["GET"])
def get_path(source, destination):
    # load graph #
    metro_graph = nx.read_graphml("../datasets/tokyometro.graphml")

    # find path #
    distance, path, path_string = path_find(metro_graph, source, destination)

    # get visualization #
    graph = visualize_path(path)
    response = {
        "distance": distance,
        "path": path,
        "path_string": path_string,
        "graph": graph,
    }
    return response
    # user output #


if __name__ == "__main__":
    app.run(debug=True)

# data, names, positions, station_lookup = load_data()
# metro = load_graph(data, positions)
# grr = path_find(metro, "A01", "S21")[1]
# print(grr)
# visualize_path(grr)
