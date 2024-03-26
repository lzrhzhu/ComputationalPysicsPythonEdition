import numpy as np
import matplotlib.pyplot as plt

def Lorentz(x, y, z, t, sigma, b, r):
    dx = sigma * (y - x)
    dy = r * x - y - x * z
    dz = x * y - b * z
    return dx, dy, dz

def Euler(x, y, z, t, dt, sigma, b, r):
    dx, dy, dz = Lorentz(x, y, z, t, sigma, b, r)
    x = x + dx * dt
    y = y + dy * dt
    z = z + dz * dt
    return x, y, z

def main():
    sigma = 10.0
    b = 8.0 / 3.0
    r_values = [5.0, 10.0, 25.0]
    dt = 0.0001
    t_values = np.arange(0.0, 50.0, dt)
    colors = ['r', 'g', 'b']

    for r, color in zip(r_values, colors):
        x, y, z = 1.0, 0.0, 0.0
        z_values = []
        for t in t_values:
            x, y, z = Euler(x, y, z, t, dt, sigma, b, r)
            z_values.append(z)
        plt.plot(t_values, z_values, color=color, label='r = ' + str(r))

    plt.legend()
    plt.title('Lorentz Attractor')
    plt.xlabel('Time')
    plt.ylabel('z')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()