# swap values
import random

a = 1
b = 2
temp = a

a = b

b = temp

print(a, b)

# make a random list of 100 numbers with values of 1 to 99

# use a list comp

random_list = [random.randrange(1, 100) for x in range(100)]
random_list2 = random_list[:]
print(random_list)

total_iterations = 0
# selection sort
for cur_pos in range(len(random_list)):
    min_pos = cur_pos
    for scan_pos in range(cur_pos + 1, len(random_list)):
        total_iterations += 1
        if random_list[scan_pos] < random_list[min_pos]:
            min_pos = scan_pos
    random_list[cur_pos], random_list[min_pos] = random_list[min_pos], random_list[cur_pos]
print(random_list)
print(total_iterations)

# iteration sort
total_iterations = 0
for key_pos in range(1, len(random_list2)):
    key_val = random_list2[key_pos]
    scan_pos = key_pos - 1  # look to dancer on left
    while scan_pos >= 0 and random_list2[scan_pos] > key_val:
        total_iterations += 1
        random_list[scan_pos + 1] = random_list2[scan_pos]
        scan_pos -= 1
        random_list2[scan_pos + 1] = key_val

print(random_list2)
print(total_iterations)

# More With Functions

print("Hello", end=" ")  # uses optional parameter which has a default value of "\n"
print("World", end="!\n")


def hello(name, time_of_day="morning"):
    print("Hello", name, "Good", time_of_day)


hello("Owen")  # morning is default

# lambda functions (anonymous function on a single line)

double_me = lambda x: x * 2
# double_me is a function that returns the value
print(double_me(9))

sum_product = lambda a, b: [a + b, a * b]

print(sum_product(3, 2))

# Real world sorting with python
my_list = [random.randrange(1, 100) for x in range(100)]
# sort method (changes the list in place)
print(my_list)
my_list.sort()  # defualt is to sort alphabetically or numerically small to large
print(my_list)
my_list.sort(reverse=True)
print(my_list)

# use a lambda as the key

my_2dlist = [[random.randrange(1, 100), random.randrange(1, 100)] for x in range(100)]
my_2dlist.sort()
print(my_2dlist)

my_2dlist.sort(key=lambda x: x[1])  # sorts by second item
print(my_2dlist)

my_2dlist.sort(key=lambda x: sum(x))
print(my_2dlist)

my_2dlist.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
print(my_2dlist)

# sorted function(returns a new list

new_list = sorted(my_2dlist, key=lambda x: sum(x))
print(new_list) # sorted by sum
print(my_2dlist) # sorted by difference
