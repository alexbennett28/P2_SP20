# recursion - function calling itself

def f():
    print("f")
    # f() # similiar to an infinite loop, but different. Causes something like a recursion depth error


f()


def g():
    print("g")
    f()


g()
f()
f()
g()
g()


# Controlling recursion with depth

def controlled(depth, max_depth):
    print("Recursion Depth:", depth)
    if depth < max_depth:
        controlled(depth + 1, max_depth)
    print("Recursion depth", depth, 'has closed')
controlled(0,10)


# Fibonacci sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# def fibonacci_recursion(n):
  #  print("Calculating Fibonacci", n)

    # base case
  #  if n == 0:
  #      return 0
   # elif n == 1:
  #      return 1
    #recursive case
  #  else:
  #      return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


# fibonacci_recursion(3)

