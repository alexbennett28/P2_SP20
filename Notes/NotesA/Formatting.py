import random

# round(number, to what digit)

print(round(2.42344343434224555966, 2))

# format method (a string method)

a = 234.53465
b = 249879249084

print("my number is {}!!" .format(a))
print(" My Numbers Are {} and {}.".format(a,b))
print(" my numbers are {1} and {0}. {1} is my favorite".format(a, b)) # you can specify the order
# numberical_order:spaceholder+justifications+sign+width+commas+precision+datatype+notation
# justification and spacing

for i in range(20):
    c = random.randrange(2000)
    # print("{:6}".format(c)) # six spaces are reserved for the number
    print("**{:^10}**".format(c)) # 30 spaces and centered

for i in range(20):
    c = random.randrange(1000000)
    print("${:8,}".format(c))

# precision and datatype (d dec/int, f float, b binary)

for i in range(20):
    c = random.random() * 1000
    print("{:14.3f}".format(c)) # 14 spaces to 3 decimals as a float

for i in range(20):
    c = random.randrange(1000)
    print("{:<10b}".format(c))

# scientific notation

for i in range(20):
    c = random.randrange(1000)
    print("{:.2e}".format(c)) # 2 decimals and then e

x = 6.77e11 # python accepts scientific notation
print(x)