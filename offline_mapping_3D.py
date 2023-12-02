# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import time

# def generate_random_direction():
#     """Generate a random 3D direction vector."""
#     return np.random.rand(3)

# def plot_trajectory(ax, points, speed):
#     """Plot the trajectory with lines connecting consecutive points."""
#     for i in range(len(points) - 1):
#         ax.plot([points[i][0], points[i+1][0]],
#                 [points[i][1], points[i+1][1]],
#                 [points[i][2], points[i+1][2]],
#                 linewidth=speed, color='blue')

# # Set the total runtime for the mapping program
# total_runtime = 30  # seconds
    
#     # Set the time interval for changing direction
# direction_change_interval = 5  # seconds
    
#     # Set the appropriate speed for drawing lines between consecutive points
# line_speed = 1.0  # You can adjust this value
    
#     # Initialize 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

#     # Initialize points list with the starting point
# points = [(0, 0, 0)]

#     # Main loop for mapping
# start_time = time.time()
# while time.time() - start_time < total_runtime:
#         # Generate a random direction every 5 seconds
#     if int(time.time() - start_time) % direction_change_interval == 0:
#         direction = generate_random_direction()

#         # Calculate the next point based on the current direction
#     last_point = points[-1]
#     new_point = (last_point[0] + direction[0],
#                      last_point[1] + direction[1],
#                      last_point[2] + direction[2])
#     points.append(new_point)

#         # Plot the trajectory
#     plot_trajectory(ax, points, line_speed)

#         # Update the plot
#     plt.pause(0.1)

#     # Show the 3D plot
# plt.show()

######################################################################

# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import time

# def generate_random_direction():
#     """Generate a random 3D direction vector."""
#     return np.random.rand(3)

# def plot_trajectory(ax, points, speed):
#     """Plot the trajectory with lines connecting consecutive points."""
#     for i in range(len(points) - 1):
#         ax.plot([points[i][0], points[i+1][0]],
#                 [points[i][1], points[i+1][1]],
#                 [points[i][2], points[i+1][2]],
#                 linewidth=speed, color='blue')

# def plot_points(ax, points):
#     """Plot red spheres at each point."""
#     for point in points:
#         ax.scatter(point[0], point[1], point[2], color='red', s=50)

# if __name__ == "__main__":
#     # Set the total runtime for the mapping program
#     total_runtime = 30  # seconds
    
#     # Set the time interval for changing direction
#     direction_change_interval = 5  # seconds
    
#     # Set the appropriate speed for drawing lines between consecutive points
#     line_speed = 1.0  # You can adjust this value
    
#     # Initialize 3D plot
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')

#     # Initialize points list with the starting point
#     points = [(0, 0, 0)]

#     # Main loop for mapping
#     start_time = time.time()
#     while time.time() - start_time < total_runtime:
#         # Generate a random direction every 5 seconds
#         if int(time.time() - start_time) % direction_change_interval == 0:
#             direction = generate_random_direction()

#         # Calculate the next point based on the current direction
#         last_point = points[-1]
#         new_point = (last_point[0] + direction[0],
#                      last_point[1] + direction[1],
#                      last_point[2] + direction[2])
#         points.append(new_point)

#         # Plot the trajectory
#         plot_trajectory(ax, points, line_speed)

#         # Plot the points
#         plot_points(ax, points)

#         # Update the plot
#         plt.pause(0.1)

#     # Show the 3D plot
#     plt.show()

######################################################################

# import matplotlib.pyplot as plt
# import numpy as np
# import time

# def generate_random_direction():
#     """Generate a random 3D direction vector."""
#     return np.random.rand(3)

# def plot_trajectory(ax, points, speed):
#     """Plot the trajectory with lines connecting consecutive points."""
#     for i in range(len(points) - 1):
#         ax.plot([points[i][0], points[i+1][0]],
#                 [points[i][1], points[i+1][1]],
#                 [points[i][2], points[i+1][2]],
#                 linewidth=speed, color='blue')

# def plot_points(ax, points):
#     """Plot red spheres at each point."""
#     for point in points:
#         ax.scatter(point[0], point[1], point[2], color='red', s=50)

# # if __name__ == "__main__":
#     # Set the total runtime for the mapping program
# total_runtime = 30  # seconds

# # Set the time interval for changing direction
# direction_change_interval = 5  # seconds

# # Set the appropriate speed for drawing lines between consecutive points
# line_speed = 1.0  # You can adjust this value

# # Initialize 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Initialize points list with the starting point
# points = [(0, 0, 0)]

# # Main loop for mapping
# start_time = time.time()
# while time.time() - start_time < total_runtime:
#     # Generate a random direction every 5 seconds
#     if int(time.time() - start_time) % direction_change_interval == 0:
#         direction = generate_random_direction()

#         # Calculate the next point based on the current direction
#         last_point = points[-1]
#         new_point = (last_point[0] + direction[0],
#                     last_point[1] + direction[1],
#                     last_point[2] + direction[2])
#         points.append(new_point)

#         # Plot the trajectory
#         plot_trajectory(ax, points, line_speed)

#         # Plot the points
#         plot_points(ax, points)

#         # Update the plot
#         plt.pause(0.1)

#     # Show the 3D plot
#     plt.show()

######################################################################

import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time

def generate_random_direction():
    # Generate a random direction in 3D space
    direction = np.random.rand(3) - 0.5  # Random values between -0.5 and 0.5
    direction /= np.linalg.norm(direction)  # Normalize to get a unit vector
    return direction

def plot_trajectory(ax, points, speed):
    """Plot the trajectory with lines connecting consecutive points."""
    for i in range(len(points) - 1):
        ax.plot([points[i][0], points[i+1][0]],
                [points[i][1], points[i+1][1]],
                [points[i][2], points[i+1][2]],
                linewidth=speed, color='blue')

def plot_points(ax, points):
    """Plot red spheres at each point."""
    for i in range(len(points)):
        # Plot only 6 red points
        if i % 5 == 0:
            ax.scatter(points[i][0], points[i][1], points[i][2], color='red', s=50)

# if __name__ == "__main__":
# Set the total runtime for the mapping program
total_runtime = 30  # seconds

# Set the time interval for changing direction
direction_change_interval = 5  # seconds

# Set the appropriate speed for drawing lines between consecutive points
line_speed = 1.0  # You can adjust this value

# Initialize 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize points list with the starting point
points = [(0, 0, 0)]

# Main loop for mapping
start_time = time.time()
while time.time() - start_time < total_runtime:
    # Generate a random direction every 5 seconds
    if int(time.time() - start_time) % direction_change_interval == 0:
        direction = generate_random_direction()

    # Calculate the next point based on the current direction
    last_point = points[-1]
    new_point = (last_point[0] + direction[0],
                    last_point[1] + direction[1],
                    last_point[2] + direction[2])
    points.append(new_point)

    # Plot the trajectory
    plot_trajectory(ax, points, line_speed)

    # Plot the points
    plot_points(ax, points)

    # Update the plot
    plt.pause(0.1)

# Show the 3D plot
plt.show()
