import networkx as nx
import json

file_path = "/Users/noahantisseril/Desktop/Projects/MetroNavigator/clean_stations.json"
with open(file_path, "r") as file:
    data = json.load(file)

file_path = "/Users/noahantisseril/Desktop/Projects/MetroNavigator/secondary.json"
with open(file_path, "r") as file:
    secondary = json.load(file)

Graph = nx.Graph()
for stations in data:
    for key in data[stations]:
        Graph.add_edge(stations, key, weight=data[stations][key])

letter_to_line = {"A" : "Rose", "I" : "Blue", "S" : "Leaf", "E" : "Magenta", "G" : "Orange", "M" : "Red", "H" : "Silver", "T" : "Sky", "C" : "Green", "Y" : "Gold", "Z" : "Purple", "N" : "Emerald", "F" : "Brown"}

start = input("Start Station: ")
end = input("End Station: ")
check = nx.shortest_path(Graph, start, end)

output = ""
for i in range(len(check) - 1):
    if i == 0:
        output += "Board at " + secondary[check[i]] + " Station. "
    if i == len(check) - 2:
        output += "Ride on the " + letter_to_line[check[i][0]] + " line until " + secondary[check[i + 1]] + " Station. "
    if check[i + 1][0] == check[i][0]:
        continue
    output += "Ride on the " + letter_to_line[check[i][0]] + " line until " + secondary[check[i]] + " Station. "
output += "Estimated time " + str(nx.path_weight(Graph, path=check, weight="weight")/60 + (40/60) * len(check)) + " minutes."
print(output)
