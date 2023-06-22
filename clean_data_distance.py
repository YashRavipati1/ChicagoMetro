import json

file_path = "stations.json"

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
            input[connection["target_id"]] = connection["distance"]
    rv[station] = input
    input = {}

# secondary = {}
# for station in data["stations"]:
#     secondary[station] = data["stations"][station]["name_en"]

with open("clean_stations_distance.json", "w") as outfile:
    json.dump(rv, outfile)
# with open("/Users/noahantisseril/Desktop/Projects/MetroNavigator/secondary.json", "w") as outfile:
#     json.dump(secondary, outfile)