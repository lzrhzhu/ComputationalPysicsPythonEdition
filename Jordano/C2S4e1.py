import vectorPlot
import numpy as np

# Constants
g = 9.81  # acceleration due to gravity, m/s^2
m = 0.194  # mass of the ball, kg
S0_over_m = 4.1e-4  # S0/m constant
w = 30 * 2 * np.pi  # angular speed, rad/s
v0 = 70 * 1609.34 / 3600  # initial speed, m/s
vd = 35  # drag speed, m/s
delta = 5  # drag coefficient
B2_over_m = lambda v: 0.0039 + 0/ (1 + np.exp((v - vd) / delta))  # drag/mass function

# Initial conditions
x, y, z = 0, 0, 0
vx, vy, vz = v0, 0, 0

# Time step
dt = 0.01

# Lists to store the trajectory
xs, ys, zs = [], [], []

# Euler's method
while x < 60 * 0.3048:  # convert 60 feet to meters
    v = np.sqrt(vx**2 + vy**2 + vz**2)
    vx += dt * (-B2_over_m(v) * v * vx - S0_over_m * vz * w)
    vy += dt * (-g)
    vz += dt * (-S0_over_m * vx * w)
    x += dt * vx
    y += dt * vy
    z += dt * vz
    xs.append(x)
    ys.append(y)
    zs.append(z)

# Convert the trajectory to feet
xs = np.array(xs) / 0.3048
ys = np.array(ys) / 0.3048
zs = np.array(zs) / 0.3048

# Plot the trajectory

line1 = ax_global.plot(xs, ys)
