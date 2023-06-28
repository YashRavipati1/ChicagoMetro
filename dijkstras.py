import sys
import json
import networkx as nx


graph = nx.read_graphml("tokyometro.graphml")
# start = sys.argv[1]
# end = sys.argv[2]

# implement all translation maps
FILE_PATH = "secondary.json"
with open(FILE_PATH, "r") as file:
    secondary = json.load(file)
tertiary = dict((v, k) for k, v in secondary.items())
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


def dijkstra(graph, start, end):
    distances = {node: 1e7 for node in graph.nodes()}
    distances[start] = 0
    pq = [(0, start)]  # priority queue of nodes to visit
    visited = set()
    previous = {}

    while len(pq) > 0:
        current_distance, current_node = pq.pop(0)

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

    path = []
    temp = end
    while temp != start:
        path.insert(0, temp)
        temp = previous[temp]

    path.insert(0, start)

    return distances[end], path


# dji = djikstra(graph, tertiary[start], tertiary[end])

# output = ""
# for i in range(len(dji[1]) - 1):
#     if i == 0:
#         output += "Board at " + secondary[dji[1][i]] + " Station. "
#     if i == len(dji[1]) - 2:
#         output += (
#             "Ride on the "
#             + letter_to_line[dji[1][i][0]]
#             + " line until "
#             + secondary[dji[1][i + 1]]
#             + " Station. "
#         )
#     if dji[1][i + 1][0] == dji[1][i][0]:
#         continue
#     output += (
#         "Ride on the "
#         + letter_to_line[dji[1][i][0]]
#         + " line until "
#         + secondary[dji[1][i]]
#         + " Station. "
#     )
# output += "Total distance traveled: " + str(dji[0]) + " km."
# print(output)
