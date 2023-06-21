import json

file_path = "/Users/noahantisseril/Desktop/Projects/MetroNavigator/stations.json"

with open(file_path, "r") as file:
    data = json.load(file)

rv = {}
input = {}
for station in data["stations"]:
    for connection in data["stations"][station]["connections"]:
        check = connection["distance"]
        if check == 0:
            input[connection["target_id"]] = 0
        else:
            input[connection["target_id"]] = (0.045 * connection["distance"] * 1000 + 23.53)
    rv[station] = input
    input = {}

print(rv)
with open("/Users/noahantisseril/Desktop/Projects/MetroNavigator/clean_stations.json", "w") as outfile:
    json.dump(rv, outfile)
    
