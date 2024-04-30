import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

num_steps = 1000

fig, ax = plt.subplots()
x, y = 0, 0
line1, = ax.plot(x, y, color='blue')

def update(i):
    # x and y between -1 and 1
    dx, dy = np.random.randint(low=-1, high=2, size=2)
    dx+=0.03 # add bias to the nutrients
    x += dx; dy += dy # upda positions
    line1.plot(x, y, color='blue')
    return line1

# animate
ani = FuncAnimation(fig=fig, func=update, frames=num_steps, interval=1)

plt.show()