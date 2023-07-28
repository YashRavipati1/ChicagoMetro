import json

file_path = "../datasets/secondary.json"

with open(file_path, "r") as file:
    data = json.load(file)

tertiary = {v: k for k, v in data.items()}
station_station = {v: v for k, v in data.items()}

with open("../datasets/tertiary.json", "w") as outfile:
    json.dump(tertiary, outfile, indent=4)
with open("../datasets/station_to_station.json", "w") as outfile:
    json.dump(station_station, outfile, indent=4)
