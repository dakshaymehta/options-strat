# Import the necessary libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes
fig = plt.figure()
ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))

# Create a random walker that moves around the screen
walker = plt.Line2D([0], [0], color='blue', marker='o', linestyle='None')

# Function to animate the walker
def animate(i):
    x, y = walker.get_xdata()[0], walker.get_ydata()[0]
    dx, dy = 0.5, 0.5
    if x + dx > 10 or x + dx < -10:
        dx = -dx
    if y + dy > 10 or y + dy < -10:
        dy = -dy
    walker.set_xdata(x + dx)
    walker.set_ydata(y + dy)
    return walker

# Create the animation
anim = animation.FuncAnimation(fig, animate, frames=100, interval=100)
plt.show()
