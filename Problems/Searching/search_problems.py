'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re

def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

# file = open('../Notes/resources/alice_in_wonderland.txt', 'r')
# print(file)
#
# for line in file:
#     print(line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

dict_list = []

with open('dictionary.txt', 'r') as f:
    for line in f:
        dict_list.append(line.strip())
    # dict_list = [x.strip() for x in f]

print(dict_list)

lengths = [len(x) for x in dict_list]
print(lengths)
maximum = max(lengths)
i = lengths.index(maximum)
print(i)
print(dict_list[i])

# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"

alice_words = []

with open("AliceInWonderLand.txt") as f:
    for line in f:
        words = split_line(line)
        for word in words:
            alice_words.append(word.upper())

print(alice_words)
# use len and sum


# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?
# count
print(alice_words.count('ALICE'))
# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"

lengths = [len(x) for x in alice_words]

print(lengths)



# use a list comp to filter out 7 letter words in alice (if len(x) == 7)

sevens = [x for x in alice_words if len(x) == 7 and "'" not in x]
print(sevens)

sevens.sort()
print(sevens)

counts = [sevens.count(x) for x in sevens]
print(counts)

print(sevens[counts.index(max(counts))])

# then use count to find out how many times each appears
# use max to find the biggest count
# index the max number to find out where it is

# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?



