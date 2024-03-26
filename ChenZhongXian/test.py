import numpy as np
import matplotlib.pyplot as plt
import scienceplots as scp


def newton_rings(radius, wavelength, R, L):
    x = np.linspace(-radius, radius, 500)
    y = np.linspace(-radius, radius, 500)
    X, Y = np.meshgrid(x, y)

    r = np.sqrt(X ** 2 + Y ** 2)
    interference = R * np.cos((2 * np.pi * r) / L)

    intensity = (2 * interference + 1) ** 2
    intensity = intensity / np.max(intensity)

    return intensity


radius = 0.1  # 牛顿环半径
wavelength = 500e-9  # 光的波长
R = 0.2  # 干涉环的反射系数
L = 1e-3  # 干涉环半径

intensity = newton_rings(radius, wavelength, R, L)

plt.imshow(intensity, cmap='hot', extent=(-radius, radius, -radius, radius))
plt.colorbar()
plt.title("Newton's Rings Interference")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.show()
