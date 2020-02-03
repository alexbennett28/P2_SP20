# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100

import random
import math
from statistics import mode

my_list = []
for i in range(101):
    my_list.append(i)
print(my_list)

# b) Make a list of even numbers from 20 to 40
my_list = []

for i in range(20, 41):
    if i % 2 == 0:
        my_list.append(i)
print(my_list)

print(my_list)
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_list = []
for i in range(101):
    my_list.append(i ** 2)
print(my_list)


# d) Make a list of all positive numbers in my_list below.
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
for num in my_list:
    if num > 0:
        print(num)


# PROBLEM 2 (Import the number list - 3pts)


# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
# Print the last 5 numbers in num_list
num_list = [2283, 5395, 1911, 1256, 9572, 3707, 9921, 4980, 5094, 7560, 2124, 7091, 1546, 2144, 7042, 9171, 8659, 9152, 6060, 5789, 5544, 3015, 4581, 8480, 6343, 3436, 7338, 2224, 9296, 5688, 3261, 3019, 4093, 2046, 2483, 1555, 2697, 4092, 3249, 2730, 2047, 9943, 7452, 2824]

print(num_list[-6:])
# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
print(max(num_list))
# Find and print the lowest number in num_list (1pt)
print(min(num_list))
my_list = [1, 2, 5, 700, 300000]


# Find and print the average of num_list (2pts)
print(sum(num_list)/len(num_list))
# Remove the lowest number from num_list (2pt)
del my_list[0]
print(my_list)
# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)
top_ten = []
# print(num_list(secondmax))



# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?
print(mode(num_list))


# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't

# Find the number of palindromes
# Hint: This may be easier to do with strings




