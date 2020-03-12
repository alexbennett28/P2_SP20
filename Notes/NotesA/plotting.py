import matplotlib.pyplot as plt

import random

plt.figure(1)  # create a new window/plot

plt.plot([1, 2, 1, 4])
plt.plot([1, 3, 5], [100, 3, 3])

plt.figure(2) # make a second window
x1 = [x for x in range(1, 101)]
y1 = [y ** 2 for y in x1]
plt.plot(x1, y1, color="green", marker="o", markersize=10, linestyle='--', alpha= .7, label="first graph")
# title axes label unit numbers key
plt.xlabel('time (seconds)')
plt.ylabel('excitement level (Yays)')
plt.axis([0, 30, 0, 20]) # [xmin, xmax, ymin, ymax]
plt.show() # opens the window




