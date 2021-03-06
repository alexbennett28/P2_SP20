import csv
import matplotlib.pyplot as plt

with open("World firearms murders and ownership - Sheet 1.tsv") as f:
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)

header = data.pop(0)
print(header)

# make a scatter plot of firearms per 100 vs homicides per 100 thousand

homicide_100k = []
firearms_100 = []
names = []
similar = ["Canada", "Norway", "Australia", "Iceland", "Finland", "Denmark", "Sweden", "Italy", "Germany", "Japan", "Singapore", "Spain", "France", "Netherlands", "United States"]
data = [x for x in data if x[0] in similar]
for country in data:
    try:
        homicides = float(country[5])
        firearms = float(country[-2])
        name = country[0]
        homicide_100k.append(homicides)
        firearms_100.append(firearms)
        names.append(name)

    except:
        print(country[0], "invalid data")

print(names)

plt.figure("Firearm Plot", figsize=(12, 6))
plt.scatter(firearms_100, homicide_100k)
plt.ylabel("homicides per 100k population")
plt.xlabel("firearms per 100 people")
plt.title("Homicides vs Gun Ownership")

plt.annotate("My text", xy=(50, 50))

for i in range(len(names)):
        plt.annotate(names[i], xy=(firearms_100[i], homicide_100k[i]))


plt.show()


