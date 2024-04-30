import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

num_steps = 1000

fig, ax = plt.subplots()
x, y = 0, 0
line1, = ax.plot(x, y, color='blue')
# Function to update the animation
def update(i):
    dx, dy = np.random.randint(low=-1, high=2, size=2)
    dx+=0.03
    x += dx; dy += dy
    line1.plot(x, y, color='blue')
    return line1

# Set up the figure and axis
ani = FuncAnimation(fig=fig, func=update, frames=num_steps, interval=1)

plt.show()