# Lists
import random
from typing import List

my_list = ["Abe", "Bev", "Cam", "Dan", "Eve", "FLo", "Gus"]
my_numlist = [5, 9, 12, 6, 3, -3, 4]

print(my_list[1])  # Bev
print(my_list[-1])  # Gus
print(my_list[:4])  # Abe to Dan as a list
print(my_list[-3:])  # Eve to Gus

my_copy = my_list  # does not create a copy
my_copy.append("Bev")
print(my_copy)
print(my_list)

# my_copy = my_list[:] # this works
# my_copy.apppend("Cam")
# print(my_copy)
# print(my_list)

# 2d lists
my_2d = [["Abe", 8], ["Bev", 7], ["Cam", 4]]
print(my_2d[1][0])
my_2d[2].append("Wilson")
print(my_2d)

# If in
if "Abe" in my_list:
    print("Abe is there")

if "abe" in my_list:
    print("abe is there")

if random.randrange(10) in [3, 5, 6, 8, 9]:
    print("yay")

# List Functions

print(len(my_list))  # returns the length of a list
print(min(my_numlist))  # returns the lowest number
print(max(my_numlist))  # returns the highest  number
# print(sum(my_list)) # sums the list

# List Methods

# print(my_list.index(["Cam"]))  # returns the index of the found object
my_list.append("Cam")  # two cams?
print(my_list.index("Cam"))  # Only returns the first one
print(my_list.count("Cam"))  # returns the number of Cam's

my_list.append("Deb")
my_list.sort()  # orders the list
print(my_list)
my_list.reverse()  # reverse the current order
print(my_list)
# manipulating the list
my_list.pop()
print(my_list)
my_person = my_list.pop()
print(my_person)
print(my_list)

# destroy an item
del my_list[1]
print(my_list)

# concatenation
first = "francis"
last = "parker"
print(first, list)
print(first + last)
print(my_list + my_numlist)
# Iterating through a list
for name in my_list:
    print(name)

# indrext variable loop

for i in range(len(my_list)):
    my_list[i] = my_list[i].upper()
    print(my_list[i])

# list comprehensions
# [returned_item FOR interator IN list/range IF filter]

# list from 50-100
my_list = []

for i in range(50, 101):
    my_list.append(i)
print(my_list)

my_list = [x for x in range(50, 101)] #does same as above
print(my_list)


# make a list of powers of 2 from 0 to 50

my_list = []

for i in range(51):
    my_list.append(2 ** i)
print(my_list)

my_list = [2 ** x for x in range(51)]

# same list, but filter out any results greater than 100000

my_list = []

for i in range(51):
    if 2 ** i < 100000:
        my_list.append(2 ** i)
print(my_list)

my_list = [2 ** x for x in range(51) if 2 ** x < 100000]
print(my_list)


# roll a single die 100 times and add it to the list

roll = random.randrange(1,7)

my_list = [random.randrange(1,7) for x in range(101)]
print(my_list)

# roll two die 100 times and add it to a list (ex: [1,6])
my_list = [ [random.randrange(1, 7), random.randrange(1, 7)] for x in range(101)]
print(my_list)

# filter out so we only show doubles ([1,1] etc.)

my_doubles = [x for x in my_list if x[0] == x[1]]
print(my_doubles)

# all at once: create a list of two die rolls, filter out the doubles
# generates two die rolls and filters out doubles
my_doubles = [x for x in [[random.randrange(1,7), random.randrange(1,7)]for x in range(100)] if x[0] == x[1]]
print(my_doubles)

# working witg strings is similar to lists

first = "Francis"
last = "Parker"
print(first[0])
first = first.upper()
print(first)
print(first + last)
print(last[-3:])
if "Par" in last:
    print("YEP")

for letter in first:
    print(letter)
