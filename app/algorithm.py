"""
    Finalized algorithm for pathfinding, uses dijkstra's.
"""


# ----------------- imports ----------------- #
import json


# ----------------- algorithm ----------------- #
"""
    Finds path + returns (path_length, path, path_string).
"""


def path_find(graph, start, end):
    # get path #
    distance, path = dijkstra(graph, start, end)

    # get path string #
    # setup
    letter_to_line = {
        "A": "Rose",
        "I": "Blue",
        "S": "Leaf",
        "E": "Magenta",
        "G": "Orange",
        "M": "Red",
        "H": "Silver",
        "T": "Sky",
        "C": "Green",
        "Y": "Gold",
        "Z": "Purple",
        "N": "Emerald",
        "F": "Brown",
    }
    with open("../datasets/secondary.json", "r") as f:
        secondary = json.load(f)

    # get string
    path_string = ""
    for i in range(len(path) - 1):
        if i == 0:
            path_string += "Board at " + secondary[path[i]] + " Station. "
        if i == len(path) - 2:
            path_string += (
                "Ride on the "
                + letter_to_line[path[i][0]]
                + " line until "
                + secondary[path[i + 1]]
                + " Station. "
            )
        if path[i + 1][0] == path[i][0]:
            continue
        path_string += (
            "Ride on the "
            + letter_to_line[path[i][0]]
            + " line until "
            + secondary[path[i + 1]]
            + " Station. "
        )
    path_string += "Total distance traveled: " + str(distance) + " km."

    # returns #
    return distance, path, path_string


"""
    Finds path.
"""


def dijkstra(graph, start, end):
    # setup dijkstra's
    distances = {node: 1e7 for node in graph.nodes()}
    distances[start] = 0
    pq = [(0, start)]  # priority queue of nodes to visit
    visited = set()
    previous = {}

    # while unvisited nodes exist
    while len(pq) > 0:
        # visit node
        current_distance, current_node = pq.pop(0)

        # break if finished
        if current_node == end:
            break
        elif current_node not in visited:
            visited.add(current_node)

            for n in graph.neighbors(current_node):
                weight = graph[current_node][n]["weight"]
                distance_to_neightbor = current_distance + weight

                if distance_to_neightbor < distances[n]:
                    distances[n] = distance_to_neightbor
                    previous[n] = current_node
                    pq.append((distance_to_neightbor, n))

    # get path
    path = []
    temp = end
    while temp != start:
        path.insert(0, temp)
        temp = previous[temp]
    path.insert(0, start)

    return distances[end], path
