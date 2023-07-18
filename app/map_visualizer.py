"""
    Visualizations for the finalized route.
"""


# ----------------- imports ----------------- #
import networkx as nx
import matplotlib.pyplot as plt
import json


# ----------------- functions ----------------- #
"""
    Visualizes a given path (assumes dijkstra's format).
"""
def visualize_path(path)
    # data & graph setup #
    # parameters
    BASE_COLOR = "0.0"

    # loading
    data, names, positions, station_lookup = load_data()
    metro = load_graph(data, positions)

    # adjust graph #
    metro, pos, labels, colors = jesus_take_the_wheel(metro, data, names, positions, station_lookup)

    # save image to load #
    nx.draw_networkx(
        metro,
        pos=pos,
        node_size=50,
        labels=labels,
        node_color=colors[0],
        edge_color=colors[1],
        with_labels=True,
        font_size=8,
    )

    plt.savefig("route.png")


"""
    What am I even reading rn. Half of this is probably not needed, 
    but I'm scared to touch it.
"""
def jesus_take_the_wheel(graph, data, names, positions, station_lookup):
    # replace
    path_expanded = []
    previous_station = None
    for station in path:
        # get associated stations
        station_name = names[station]
        if station_name == previous_station:
            continue

        try:
            intersecting_stations = station_lookup[station_name]
        except KeyError:
            continue
        previous_station = station_name

        # add
        path_expanded += intersecting_stations

    
    # get attributes #
    nodes = graph.nodes(data=True)
    edges = graph.edges(data=True)
    color_map_nodes = [BASE_COLOR] * len(nodes)
    color_map_edges = [BASE_COLOR] * len(edges)

    # labels
    names_path = {
        key: value for key, value in names.items() if key in nodes and key in path
    }

    nodes_list = list(graph.nodes())
    edges_list = list(graph.edges())
    # node colors for only path
    for node in path:
        color_map_nodes[nodes_list.index(node)] = positions[node][2]
        station_name = names_path[node]
        try:
            intersecting_stations = station_lookup[station_name]
        except KeyError:
            continue
        for station in intersecting_stations:
            color_map_nodes[nodes_list.index(station)] = positions[node][2]

    # edge colors for only path
    for start, end in zip(path, path[1:]):
        edge = (start, end)
        station_name1 = names[edge[0]]
        station_name2 = names[edge[1]]
        try:
            color_map_edges[edges_list.index(edge)] = color_map_nodes[
                nodes_list.index(edge[0])
            ]
        except ValueError:
            color_map_edges[edges_list.index((edge[1], edge[0]))] = color_map_nodes[
                nodes_list.index(edge[0])
            ]
        try:
            intersecting_stations1 = station_lookup[station_name1]
            intersecting_stations2 = station_lookup[station_name2]
        except KeyError:
            continue
        for station1 in intersecting_stations1:
            for station2 in intersecting_stations2:
                inter_edge = (station1, station2)
                if inter_edge in edges_list:
                    color_map_edges[edges_list.index(inter_edge)] = color_map_nodes[
                        nodes_list.index(edge[0])
                    ]

    for i in path:
        station_name = names_path[i]
        try:
            intersecting_stations = station_lookup[station_name]
        except KeyError:
            continue

    pos = nx.get_node_attributes(graph, "pos")
    check = path[0][0]

    hold = []
    hold.append(path[0])
    for i in range(len(path)):
        if path[i][0] != check:
            hold.append(path[i])
            check = path[i][0]
    if path[len(path) - 1] not in hold:
        hold.append(path[len(path) - 1])

    node_label_dict = {}
    for i in hold:
        node_label_dict[i] = secondary[i]
    nx.set_node_attributes(graph, node_label_dict, 'label')

    return graph, pos, node_label_dict, [color_map_nodes, color_map_edges]


"""
    Initializes graph.
"""
def load_graph(data, positions):
    # define graph
    graph = nx.Graph()
        
    # load with positions
    for node, neighbors in data.items():
        graph.add_node(node, pos=(positions[node][0], positions[node][1]))
        for neighbor, weight in neighbors.items():
            graph.add_edge(node, neighbor, weight=weight)


"""
    Loads data necessary for visualizing.
"""
def load_data():
    # load datasets
    with open("../datasets/clean_stations.json") as f:
        data = json.load(f)
    with open("../datasets/secondary.json", "r") as f:
        names = json.load(f)
    with open("../datasets/station_positions.json", "r") as f:
        positions = json.load(f)
    with open("../datasets/full_intersections.json", "r") as f:
        station_lookup = json.load(f)
    
    # adjust data
    station_lookup = {k: list(v.keys()) for k, v in station_lookup.items()}
    for i in positions:
        positions[i][1] = 1785 - positions[i][1]
    
    # return
    return data, names, positions, station_lookup

