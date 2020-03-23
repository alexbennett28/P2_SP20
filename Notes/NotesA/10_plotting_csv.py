import csv
import matplotlib.pyplot as plt

with open("../Libraries_-_2019_Visitors_by_Location (1).csv") as f:
    reader = csv.reader(f)  # makes a reader object
    data = list(reader)
print(data)

header = data.pop(0)
print(header)

# print(data[0])
# month_names = [x[0] for x in data]

# sulzer_index = names.index("Sulzer Regional Library")
# print(sulzer_index)
# month_numbers = [x for x in data(12)]
# month_names = header[4:-1]
# print(month_names)

# plt.figure(1, tight_layout=True) # tight_fit makes everything fit in figure

# plt.title("Sulzer Visitors By Month", color="blue")
# plt.ylabel("Visitors")
# plt.xticks(month_numbers, month_names, rotation=45)
# plt.bar(month_numbers, sultzer_by_month)
# plt.axes([-1, 13, 3, 15]) # xin, xmax, ymin, ymax

# starting over with just headers and data

# plot top ten libraries for YTD totals
plt.figure(2, tight_layout=True, figsize=(14, 6))  # fig size is how wide you want it in inches
print(header)

data.sort(key=lambda x: int(x[-1]))
data(print)

top_ten = data[-10:]
top_ten_ytd = [int(x[-1]) for x in top_ten]

top_ten_names = [x[0] for x in top_ten]

x_vals = [x for x in range(len(top_ten))]
plt.bar(x_vals, top_ten_ytd)  # barh is a horizontal bar graph
plt.xticks(x_vals, top_ten_names, fontsize=10)

plt.xlabel("Visitor YTD")
plt.title("Top ten Most Visited Chicago Libraries")
