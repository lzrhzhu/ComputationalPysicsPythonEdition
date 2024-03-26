import numpy as np
import matplotlib.pyplot as plt
import random

# 设置模拟空间的大小
size = 101  # 使用奇数大小以便有中心点
space = np.zeros((size, size))

# 在中心放置一个初始团簇
center = size // 2
space[center, center] = 1

def walk(space):
    # 选择一个随机的起始位置
    x, y = random.choice([(center, 0), (0, center), (center, size - 1), (size - 1, center)])
    # 进行随机行走直到粒子接触到团簇
    while True:
        # 随机选择方向
        dx, dy = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        x += dx
        y += dy
        # 如果粒子走出了模拟空间，重新开始
        if x < 0 or x >= size or y < 0 or y >= size:
            return walk(space)
        # 检查是否接触到团簇
        if (space[max(x - 1, 0):min(x + 2, size), max(y - 1, 0):min(y + 2, size)] == 1).any():
            space[x, y] = 1
            break
# 模拟团簇生长
particles = 740  # 设置粒子数量
for _ in range(particles):
    walk(space)
# 可视化模拟结果
plt.figure(figsize=(10, 10))
plt.imshow(space, cmap='Greys', interpolation='nearest')
plt.title('Diffusion-Limited Aggregation')
plt.axis('off')
plt.show()
def calculate_mass(radius, space, center):
    """计算给定半径内的质量（被占据的位置数量）。"""
    y, x = np.ogrid[-center:size - center, -center:size - center]
    mask = x ** 2 + y ** 2 <= radius ** 2
    return np.sum(space[mask])
def fractal_dimension(space, center):
    """计算分形维数。"""
    radii = np.arange(1, center-15)
    masses = [calculate_mass(r, space, center) for r in radii]
    logs_r = np.log(radii)
    logs_m = np.log(masses)
    # 使用线性回归来估计斜率，即分形维数
    fit = np.polyfit(logs_r, logs_m, 1)
    plt.plot(logs_r, logs_m)
    plt.show()
    return fit[0]

d = fractal_dimension(space, center)
print(f"Estimated fractal dimension: {d}")