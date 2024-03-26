import matplotlib.pyplot as plt
import numpy as np

def koch_segment(p1, p2, order):
    if order == 0:
        # Base case: just draw a line segment
        return np.array([p1, p2])
    else:
        # Calculate the three intermediate points
        p1_p2 = p2 - p1
        p3 = p1 + p1_p2 / 3
        p5 = p1 + p1_p2 * 2 / 3

        # Calculate the fourth point with rotation
        theta = np.deg2rad(60)  # 角度转换为弧度
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                   [np.sin(theta), np.cos(theta)]])
        p4 = p3 + np.dot(rotation_matrix, p1_p2 / 3)

        # Recursively calculate the segments
        return np.concatenate([
            koch_segment(p1, p3, order - 1),
            koch_segment(p3, p4, order - 1),
            koch_segment(p4, p5, order - 1),
            koch_segment(p5, p2, order - 1)
        ])

def koch_snowflake(order):
    # Initial triangle vertices
    vertices = np.array([[0, 0],
                         [0.5, np.sin(np.pi / 3)],
                         [1, 0],
                         [0, 0]])

    # Apply the koch_segment function to each side of the triangle
    snowflake = np.concatenate([
        koch_segment(vertices[i], vertices[i + 1], order) for i in range(3)
    ])

    return snowflake

# Set the order of the Koch snowflake
order = 6

# Generate the Koch snowflake points
snowflake = koch_snowflake(order)

# Plot the Koch snowflake
plt.figure(figsize=(8, 8))
plt.plot(snowflake[:, 0], snowflake[:, 1], 'b')
plt.axis('equal')
plt.axis('off')  # Turn off the axis
plt.show()