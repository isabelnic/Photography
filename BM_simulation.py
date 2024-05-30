import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation 
from datetime import datetime as dt
import cv2
import os

num_steps = 1001

fig, ax = plt.subplots()
# plt.axis('off')
global x, y
x, y = [0], [0]
line1, = ax.plot(0, 0, lw=0.5)
ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.set_title('Brownian Motion of a Particle Path', fontsize=14)


def brownian_motion(num_steps, start_pos, xbias=0, ybias=0):
    position = np.zeros((2, num_steps+1))  # Initialize array
    position[0, 0], position[1, 0] = start_pos[0], start_pos[1]  # Set initial position
    x, y = np.random.randint(low=-1, high=2, size=num_steps), np.random.randint(low=-1, high=2, size=num_steps)
    position[0, 1:] = x + xbias  # Generate random steps in x
    position[1, 1:] = y + ybias  # Generate random steps in y
    position = np.cumsum(position, axis=1)  # Take cumulative sum to get position
    return position


pos = brownian_motion(num_steps, start_pos=[0, 0])

# def update(i):
#     line1.set_data(pos[0, 0:i], pos[1, 0:i])
#     return line1,

## animate ##
# anim = FuncAnimation(fig=fig, func=update, frames=1000, interval=200,
#                     blit=True)
# fig.suptitle('Brownian motion particle path', fontsize=14) 
# saving to m4 using ffmpeg writer 
# writergif = animation.FFMpegWriter(fps=300) #animation.PillowWriter(fps=200)
now = dt.now().strftime("%Y-%m-%d_%H-%M-%S")
# anim.save(f'BM_animation_{now}.mp4',writer=writergif, dpi=300)



