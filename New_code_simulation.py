import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to calculate the distance and angle from origin to the random position
def calculate_distance_angle(x1, y1, x2, y2):
    r = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    theta = np.arctan2(y2 - y1, x2 - x1)
    return r, theta

# Function to calculate the distance from the tip of the arm to the random position
def distance_from_tip(x, y, tip_x, tip_y):
    distance = np.sqrt((x - tip_x)**2 + (y - tip_y)**2)
    return distance

# Define the origin (initial position of the arm)
origin_x = 5
origin_y = -5

# Define the box (trolley/wagon) in the first quadrant
box_x_min = 2
box_x_max = 12
box_y_min = 2
box_y_max = 8

# Generate a random position within the box
x_random = np.random.uniform(box_x_min, box_x_max)
y_random = np.random.uniform(box_y_min, box_y_max)

# Simulation parameters
fixed_arm_length = 7.5  # Fixed length of the first arm

# Calculate distance and angle from origin to the random position
r, theta = calculate_distance_angle(origin_x, origin_y, x_random, y_random)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_aspect('equal')
ax.grid(True)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Arm Simulation')

# Plot the random position
random_pos, = ax.plot([x_random], [y_random], 'ro', label='Random Position')

# Plot the origin
origin_pos, = ax.plot([origin_x], [origin_y], 'go', label='Origin')

# Plot the box
box, = ax.plot([box_x_min, box_x_max, box_x_max, box_x_min, box_x_min],
               [box_y_min, box_y_min, box_y_max, box_y_max, box_y_min], 'k-', label='Box')

# Plot the arm
arm_line, = ax.plot([], [], 'b-', lw=2, label='Arm')

# Plot the second segment of the arm
second_arm_line, = ax.plot([], [], 'y-', lw=2, label='Second Arm')

# Plot the tip of the arm
tip_of_arm, = ax.plot([], [], 'bo')

# Initialize function for animation
def init():
    arm_line.set_data([], [])
    second_arm_line.set_data([], [])
    tip_of_arm.set_data([], [])
    return arm_line, second_arm_line, tip_of_arm

# Update function for animation
def update(frame):
    angle_step = np.linspace(0, theta, 100)
    if frame < len(angle_step):
        # Rotate the fixed-length arm to the calculated angle
        current_angle = angle_step[frame]
        x = origin_x + fixed_arm_length * np.cos(current_angle)
        y = origin_y + fixed_arm_length * np.sin(current_angle)
        arm_line.set_data([origin_x, x], [origin_y, y])
        tip_of_arm.set_data(x, y)
        second_arm_line.set_data([], [])
    else:
        # Extend the second arm towards the random point
        x = origin_x + fixed_arm_length * np.cos(theta)
        y = origin_y + fixed_arm_length * np.sin(theta)
        arm_line.set_data([origin_x, x], [origin_y, y])
        tip_of_arm.set_data(x, y)
        
        remaining_distance = distance_from_tip(x_random, y_random, x, y)
        remaining_angle = np.arctan2(y_random - y, x_random - x)
        
        if frame - len(angle_step) < remaining_distance:
            new_x = x + (frame - len(angle_step)) * np.cos(remaining_angle)
            new_y = y + (frame - len(angle_step)) * np.sin(remaining_angle)
        else:
            new_x = x_random
            new_y = y_random
        
        second_arm_line.set_data([x, new_x], [y, new_y])
        tip_of_arm.set_data(new_x, new_y)
    
    return arm_line, second_arm_line, tip_of_arm

# Calculate total frames needed for the animation
extension_frames = 100  # number of frames to rotate the arm
remaining_distance = distance_from_tip(x_random, y_random, origin_x + fixed_arm_length * np.cos(theta), origin_y + fixed_arm_length * np.sin(theta))
extension_steps = int(remaining_distance) + 20  # additional steps to cover the extension smoothly
total_frames = extension_frames + extension_steps

ani = FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=True, repeat=False)

# Show the plot
plt.legend()
plt.show()





# # import numpy as np
# # import matplotlib.pyplot as plt
# # from matplotlib.animation import FuncAnimation

# # # Function to calculate the distance and angle from origin to the random position
# # def calculate_distance_angle(x1, y1, x2, y2):
# #     r = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# #     theta = np.arctan2(y2 - y1, x2 - x1)
# #     return r, theta

# # # Function to calculate the distance from the tip of the arm to the random position
# # def distance_from_tip(x, y, tip_x, tip_y):
# #     distance = np.sqrt((x - tip_x)**2 + (y - tip_y)**2)
# #     return distance

# # # Define the origin (initial position of the arm)
# # origin_x = -5
# # origin_y = -5

# # # Define the box (trolley/wagon) in the first quadrant
# # box_x_min = 2
# # box_x_max = 12
# # box_y_min = 2
# # box_y_max = 8

# # # Generate a random position within the box
# # x_random = np.random.uniform(box_x_min, box_x_max)
# # y_random = np.random.uniform(box_y_min, box_y_max)

# # # Simulation parameters
# # arm_length = np.sqrt((box_x_min - origin_x)**2 + (box_y_min - origin_y)**2)

# # # Calculate distance and angle from origin to the random position
# # r, theta = calculate_distance_angle(origin_x, origin_y, x_random, y_random)

# # # Use the calculated angle for the arm
# # arm_angle = theta

# # # Create a figure and axis
# # fig, ax = plt.subplots()
# # ax.set_xlim(-20, 20)
# # ax.set_ylim(-20, 20)
# # ax.set_aspect('equal')
# # ax.grid(True)
# # ax.set_xlabel('X-axis')
# # ax.set_ylabel('Y-axis')
# # ax.set_title('Arm Simulation')

# # # Plot the random position
# # random_pos, = ax.plot([x_random], [y_random], 'ro', label='Random Position')

# # # Plot the origin
# # origin_pos, = ax.plot([origin_x], [origin_y], 'go', label='Origin')

# # # Plot the box
# # box, = ax.plot([box_x_min, box_x_max, box_x_max, box_x_min, box_x_min],
# #                [box_y_min, box_y_min, box_y_max, box_y_max, box_y_min], 'k-', label='Box')

# # # Plot the arm
# # arm_line, = ax.plot([], [], 'b-', lw=2, label='Arm')

# # # Plot the second segment of the arm
# # second_arm_line, = ax.plot([], [], 'g-', lw=2, label='Second Arm')

# # # Plot the tip of the arm
# # tip_of_arm, = ax.plot([], [], 'bo')

# # # Initialize function for animation
# # def init():
# #     arm_line.set_data([], [])
# #     second_arm_line.set_data([], [])
# #     tip_of_arm.set_data([], [])
# #     return arm_line, second_arm_line, tip_of_arm

# # # Update function for animation
# # def update(frame):
# #     if frame <= arm_length:
# #         x = origin_x + frame * np.cos(arm_angle)
# #         y = origin_y + frame * np.sin(arm_angle)
# #         arm_line.set_data([origin_x, x], [origin_y, y])
# #         tip_of_arm.set_data(x, y)
# #         second_arm_line.set_data([], [])
# #     else:
# #         x = origin_x + arm_length * np.cos(arm_angle)
# #         y = origin_y + arm_length * np.sin(arm_angle)
# #         arm_line.set_data([origin_x, x], [origin_y, y])
# #         tip_of_arm.set_data(x, y)
        
# #         remaining_distance = distance_from_tip(x_random, y_random, x, y)
# #         remaining_angle = np.arctan2(y_random - y, x_random - x)
        
# #         new_x = x + (frame - arm_length) * np.cos(remaining_angle)
# #         new_y = y + (frame - arm_length) * np.sin(remaining_angle)
        
# #         if remaining_distance < frame - arm_length:
# #             new_x = x_random
# #             new_y = y_random
        
# #         second_arm_line.set_data([x, new_x], [y, new_y])
# #         tip_of_arm.set_data(new_x, new_y)
    
# #     return arm_line, second_arm_line, tip_of_arm

# # # Animate the arm moving and extending
# # total_distance = np.sqrt((x_random - (origin_x + arm_length * np.cos(arm_angle)))**2 + 
# #                          (y_random - (origin_y + arm_length * np.sin(arm_angle)))**2)
# # frames = np.linspace(0, arm_length + total_distance, 200)
# # ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, repeat=False)

# # # Show the plot
# # plt.legend()
# # plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Function to calculate the distance and angle from origin to the random position
# def calculate_distance_angle(x1, y1, x2, y2):
#     r = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#     theta = np.arctan2(y2 - y1, x2 - x1)
#     return r, theta

# # Function to calculate the distance from the tip of the arm to the random position
# def distance_from_tip(x, y, tip_x, tip_y):
#     distance = np.sqrt((x - tip_x)**2 + (y - tip_y)**2)
#     return distance

# # Define the origin (initial position of the arm)
# origin_x = 5
# origin_y = -5

# # Define the box (trolley/wagon) in the first quadrant
# box_x_min = 2
# box_x_max = 12
# box_y_min = 2
# box_y_max = 8

# # Generate a random position within the box
# x_random = np.random.uniform(box_x_min, box_x_max)
# y_random = np.random.uniform(box_y_min, box_y_max)

# # Simulation parameters
# fixed_arm_length = 7.5  # Fixed length of the first arm

# # Calculate distance and angle from origin to the random position
# r, theta = calculate_distance_angle(origin_x, origin_y, x_random, y_random)

# # Create a figure and axis
# fig, ax = plt.subplots()
# ax.set_xlim(-20, 20)
# ax.set_ylim(-20, 20)
# ax.set_aspect('equal')
# ax.grid(True)
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_title('Arm Simulation')

# # Plot the random position
# random_pos, = ax.plot([x_random], [y_random], 'ro', label='Random Position')

# # Plot the origin
# origin_pos, = ax.plot([origin_x], [origin_y], 'go', label='Origin')

# # Plot the box
# box, = ax.plot([box_x_min, box_x_max, box_x_max, box_x_min, box_x_min],
#                [box_y_min, box_y_min, box_y_max, box_y_max, box_y_min], 'k-', label='Box')

# # Plot the arm
# arm_line, = ax.plot([], [], 'b-', lw=2, label='Arm')

# # Plot the second segment of the arm
# second_arm_line, = ax.plot([], [], 'y-', lw=2, label='Second Arm')

# # Plot the tip of the arm
# tip_of_arm, = ax.plot([], [], 'bo')

# # Initialize function for animation
# def init():
#     arm_line.set_data([], [])
#     second_arm_line.set_data([], [])
#     tip_of_arm.set_data([], [])
#     return arm_line, second_arm_line, tip_of_arm

# # Update function for animation
# def update(frame):
#     angle_step = np.linspace(0, theta, 100)
#     if frame < len(angle_step):
#         # Rotate the fixed-length arm to the calculated angle
#         current_angle = angle_step[frame]
#         x = origin_x + fixed_arm_length * np.cos(current_angle)
#         y = origin_y + fixed_arm_length * np.sin(current_angle)
#         arm_line.set_data([origin_x, x], [origin_y, y])
#         tip_of_arm.set_data(x, y)
#         second_arm_line.set_data([], [])
#     else:
#         # Extend the second arm towards the random point
#         x = origin_x + fixed_arm_length * np.cos(theta)
#         y = origin_y + fixed_arm_length * np.sin(theta)
#         arm_line.set_data([origin_x, x], [origin_y, y])
#         tip_of_arm.set_data(x, y)
        
#         remaining_distance = distance_from_tip(x_random, y_random, x, y)
#         remaining_angle = np.arctan2(y_random - y, x_random - x)
        
#         if frame - len(angle_step) < remaining_distance:
#             new_x = x + (frame - len(angle_step)) * np.cos(remaining_angle)
#             new_y = y + (frame - len(angle_step)) * np.sin(remaining_angle)
#         else:
#             new_x = x_random
#             new_y = y_random
        
#         second_arm_line.set_data([x, new_x], [y, new_y])
#         tip_of_arm.set_data(new_x, new_y)
    
#     return arm_line, second_arm_line, tip_of_arm

# # Calculate total frames needed for the animation
# total_frames = 100 + int(np.sqrt((x_random - (origin_x + fixed_arm_length * np.cos(theta)))**2 + 
#                                  (y_random - (origin_y + fixed_arm_length * np.sin(theta)))**2))

# ani = FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=True, repeat=False)

# # Show the plot
# plt.legend()
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Function to calculate the distance and angle from origin to the random position
# def calculate_distance_angle(x1, y1, x2, y2):
#     r = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#     theta = np.arctan2(y2 - y1, x2 - x1)
#     return r, theta

# # Function to calculate the distance from the tip of the arm to the random position
# def distance_from_tip(x, y, tip_x, tip_y):
#     distance = np.sqrt((x - tip_x)**2 + (y - tip_y)**2)
#     return distance

# # Define the origin (initial position of the arm)
# origin_x = 5
# origin_y = -5

# # Define the box (trolley/wagon) in the first quadrant
# box_x_min = 2
# box_x_max = 12
# box_y_min = 2
# box_y_max = 8

# # Generate a random position within the box
# x_random = np.random.uniform(box_x_min, box_x_max)
# y_random = np.random.uniform(box_y_min, box_y_max)

# # Simulation parameters
# fixed_arm_length = 7.5  # Fixed length of the first arm

# # Calculate distance and angle from origin to the random position
# r, theta = calculate_distance_angle(origin_x, origin_y, x_random, y_random)

# # Create a figure and axis
# fig, ax = plt.subplots()
# ax.set_xlim(-20, 20)
# ax.set_ylim(-20, 20)
# ax.set_aspect('equal')
# ax.grid(True)
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_title('Arm Simulation')

# # Plot the random position
# random_pos, = ax.plot([x_random], [y_random], 'ro', label='Random Position')

# # Plot the origin
# origin_pos, = ax.plot([origin_x], [origin_y], 'go', label='Origin')

# # Plot the box
# box, = ax.plot([box_x_min, box_x_max, box_x_max, box_x_min, box_x_min],
#                [box_y_min, box_y_min, box_y_max, box_y_max, box_y_min], 'k-', label='Box')

# # Plot the arm
# arm_line, = ax.plot([], [], 'b-', lw=2, label='Arm')

# # Plot the second segment of the arm
# second_arm_line, = ax.plot([], [], 'y-', lw=2, label='Second Arm')

# # Plot the tip of the arm
# tip_of_arm, = ax.plot([], [], 'bo')

# # Initialize function for animation
# def init():
#     arm_line.set_data([], [])
#     second_arm_line.set_data([], [])
#     tip_of_arm.set_data([], [])
#     return arm_line, second_arm_line, tip_of_arm

# # Update function for animation
# def update(frame):
#     angle_step = np.linspace(0, theta, 100)
#     if frame < len(angle_step):
#         # Rotate the fixed-length arm to the calculated angle
#         current_angle = angle_step[frame]
#         x = origin_x + fixed_arm_length * np.cos(current_angle)
#         y = origin_y + fixed_arm_length * np.sin(current_angle)
#         arm_line.set_data([origin_x, x], [origin_y, y])
#         tip_of_arm.set_data(x, y)
#         second_arm_line.set_data([], [])
#     else:
#         # Extend the second arm towards the random point
#         x = origin_x + fixed_arm_length * np.cos(theta)
#         y = origin_y + fixed_arm_length * np.sin(theta)
#         arm_line.set_data([origin_x, x], [origin_y, y])
#         tip_of_arm.set_data(x, y)
        
#         remaining_distance = distance_from_tip(x_random, y_random, x, y)
#         remaining_angle = np.arctan2(y_random - y, x_random - x)
        
#         if frame - len(angle_step) < remaining_distance:
#             new_x = x + (frame - len(angle_step)) * np.cos(remaining_angle)
#             new_y = y + (frame - len(angle_step)) * np.sin(remaining_angle)
#         else:
#             new_x = x_random
#             new_y = y_random
        
#         second_arm_line.set_data([x, new_x], [y, new_y])
#         tip_of_arm.set_data(new_x, new_y)
    
#     return arm_line, second_arm_line, tip_of_arm

# # Calculate total frames needed for the animation
# total_frames = 120 + int(np.sqrt((x_random - (origin_x + fixed_arm_length * np.cos(theta)))**2 + 
#                                  (y_random - (origin_y + fixed_arm_length * np.sin(theta)))**2))

# ani = FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=True, repeat=False)

# # Show the plot
# plt.legend()
# plt.show()


