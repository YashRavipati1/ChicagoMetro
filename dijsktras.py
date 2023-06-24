import networkx as nx
import sys


graph = nx.read_graphml('tokyometro.graphml')
start = sys.argv[1]
end = sys.argv[2]


def djikstra(graph, start, end):
    distances = {node: 1e7 for node in graph.nodes()}
    distances[start] = 0 
    pq = [(0, start)] #priority queue of nodes to visit
    visited = set()
    previous = {}

    while len(pq) > 0:
        current_distance, current_node = pq.pop(0)

        if current_node == end:
            break
        elif current_node not in visited:
            visited.add(current_node)

            for n in graph.neighbors(current_node):
                weight = graph[current_node][n]['weight']
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


dji = djikstra(graph, start, end)
print(dji)