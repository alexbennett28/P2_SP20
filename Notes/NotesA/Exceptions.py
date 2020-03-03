# Exceptions

# Exception - condition that results in abnormal program flow

# Throw/ Raise- Abnormal conditions throw or raise an exception
# Catch- Code that handles the abnormal condition

# unhandled exceptions - program killers. Thrown but not caught

# Divide by zero error(ZeroDivisionError)

x = 0

y = 2

try:
    print(x/y)
except:
    print("Invalid operation, divide by zero")


# Conversion error (valueError)

try:
    user_input = int(input("Enter a valid integer"))
    done = True
except:
    print("Number not valid, enter an integer")

# File opening (IOError, FileNotFoundError)

try:
    file = open("AliceInWonderland.txt")

except:
    print("File not found")

# use the built in error types for python

try:
    my_file = open("myfile.txt")

except FileNotFoundError:
    print("file not found")
except ZeroDivisionError:
    print("zero division error")
except ValueError:
    print("Invalid int conversion")
except:
    print("unknown error")

# make an mpg calculator

try:
    miles = float(input("Miles Traveled: "))
    gallons = float(input("gallons used: "))
except ValueError:
    print("You entered an invalid number")
finally:
    print("Finally will always run regardless of exception or no exception")



print("Mpg is", miles / gallons)


