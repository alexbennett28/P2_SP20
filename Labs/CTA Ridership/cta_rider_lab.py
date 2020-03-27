import matplotlib.pyplot as plt
import csv
'''
CTA Ridership (25pts)

Get the csv from the following data set.https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD

This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)
'''

with open('CTA_-_Ridership_-_Annual_Boarding_Totals (1).csv') as f:
    reader = csv.reader(f)
    data = list(reader)




lten_years = [x[0] for x in data[-10:]]
print(lten_years)
last_ten_bus = [x[1] for x in data[-10:]]
last_ten_train = [x[3] for x in data[-10:]]

last_ten_total = [x[4] for x in data[-10:]]







plt.figure(1, tight_layout=True)
bus = plt.plot(lten_years, last_ten_bus, label="Bus Passengers")
train = plt.plot(lten_years, last_ten_train, label="Train Passengers")
total = plt.plot(lten_years, last_ten_total, label="Total Passengers")

plt.xlabel("Years")
plt.ylabel("Amount of People on Each Transit System")

plt.title("CTA Ridership Per Year")

plt.legend()
plt.show()


# Despite the rise of ride-share apps like Uber, the CTA has seen a revival of sorts. My thinking is that Uber has forced more people to have an increased appreciation for cheap ways to get back and forth. Also, you hear a lot about how broke millenials are, so it is quite possible that they use CTA more than the previous generation and have been boosint the CTA's numbers.
