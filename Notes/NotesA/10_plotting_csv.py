import csv
import matplotlib.pyplot as plt

with open("../Libraries_-_2019_Visitors_by_Location (1).csv") as f:
    reader = csv.reader(f)  # makes a reader object
    data = list(reader)
print(data)

header = data.pop(0)
print(header)

print(data[0])
names = [x[0] for x in data]

sulzer_index = names.index("Sulzer Regional Library")
print(sulzer_index)
