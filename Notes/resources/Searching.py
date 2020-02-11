# Searching

# use forward slashes to go into folders and ".." to go up a folder

file = open('../resources/super_villains.txt', 'r')  # open to read
print(file)

for line in file:
    print(line)

file.close()

# .strip() method removes the extra characters at the end of the text

print("     hello".strip())

print("World\n")
print("World\n".strip())
print("world")

# w overrides
# a opens to append
file = open('../resources/super_villains.txt', 'a')
file.write('Lee the Merciless\n')
file.write('Rohan the Destroyer\n')
file.close()

# open to write can create a new file

file = open('../resources/heroes.txt', 'w')

file.write('Owen the Valiant\n')

file.close()

# Better way to open close a file (syntactic sugar)
with open('../resources/super_villains.txt') as f:
    for line in f:
        print(line.strip())

with open('../resources/super_villains.txt') as f:
    read_data = f.read()  # big string

print("\n\nRead method")

print(read_data)

# reading data into an array (list)

with open('../resources/super_villains.txt', 'r') as f:
    villains = [x.strip().upper() for x in f]
print(villains)

# Linear Search  (not efficient, but easy)

key = "Vidar the Manic".upper()

i = 0
while i < len(villains) - 1 and key != villains[i]:
    i += 1

if i < len(villains):
    print("found it at position", i)
else:
    print(key, "is not in the list")


def linear_search(key, my_list):

    """

    :param key: what you are looking for

    :param list: where you are looking
    :return: bool did you find it
    """

    i = 0
    while i < (len(my_list) - 1) and key.upper() != my_list[i]:
        i += 1
    if i < len(villains) - 1:
        print("found", key, "at position", i)
        return True
    else:
        print(key, "not found.")
        return False


# binary search

key = "THEODORA THE WOCKED"
lower_bound = 0

upper_bound = len(villains)

found = False


while lower_bound <= upper_bound and not found:
    middle_pos = (upper_bound + lower_bound) // 2

    if villains[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villains[middle_pos] > key:
        upper_bound = middle_pos - 1

    else:
        found = True

if found:
    print(key, "was found at position", middle_pos)
else:
    print(key, "was not found.")
    
