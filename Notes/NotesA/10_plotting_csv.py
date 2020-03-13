import csv
import matplotlib.pyplot as plt

with open("../Libraries_-_2019_Visitors_by_Location (1).csv") as f:
    reader = csv.reader(f)  # makes a reader object
    data = list(reader)
print(data)

header = data.pop(0)
print(header)

print(data[0])
month_names = [x[0] for x in data]

sulzer_index = names.index("Sulzer Regional Library")
print(sulzer_index)
month_numbers = [x for x in data(12)]
month_names = header[4:-1]
print(month_names)

plt.figure(1, tight_layout=True) # tight_fit makes everything fit in figure

plt.title("Sulzer Visitors By Month")
plt.ylabel("Visitors")
plt.xticks(month_numbers, month_names, rotation=45)


