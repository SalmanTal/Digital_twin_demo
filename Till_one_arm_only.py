import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to calculate the distance and angle from origin to the random position
def calculate_distance_angle(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

# Function to calculate the distance from the tip of the arm to the random position
def distance_from_tip(x, y, arm_length, arm_angle):
    tip_x = arm_length * np.cos(arm_angle)
    tip_y = arm_length * np.sin(arm_angle)
    distance = np.sqrt((x - tip_x)**2 + (y - tip_y)**2)
    return distance

# Get user input for the random position
x_random = float(input("Enter the x-coordinate of the random position: "))
y_random = float(input("Enter the y-coordinate of the random position: "))

# Simulation parameters
arm_length = 5

# Calculate distance and angle from origin to the random position
r, theta = calculate_distance_angle(x_random, y_random)

# Use the calculated angle for the arm
arm_angle = theta

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-arm_length-1, x_random + 1)
ax.set_ylim(-arm_length-1, y_random + 1)
ax.set_aspect('equal')
ax.grid(True)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Arm Simulation')

# Plot the random position
random_pos, = ax.plot([x_random], [y_random], 'ro', label='Random Position')

# Plot the arm
arm_line, = ax.plot([], [], 'b-', lw=2, label='Arm')

# Plot the tip of the arm
tip_of_arm, = ax.plot([], [], 'bo')

# Initialize function for animation
def init():
    arm_line.set_data([], [])
    tip_of_arm.set_data([], [])
    return arm_line, tip_of_arm

# Update function for animation
def update(frame):
    if frame <= arm_length:
        x = frame * np.cos(arm_angle)
        y = frame * np.sin(arm_angle)
    else:
        x = arm_length * np.cos(arm_angle)
        y = arm_length * np.sin(arm_angle)
    
    arm_line.set_data([0, x], [0, y])
    tip_of_arm.set_data(x, y)
    return arm_line, tip_of_arm

# Animate the arm moving and extending
frames = np.linspace(0, arm_length, 100)
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, repeat=False)

# Show the plot
plt.legend()
plt.show()