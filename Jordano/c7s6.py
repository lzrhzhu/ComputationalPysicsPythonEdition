import numpy as np
import matplotlib.pyplot as plt
import random

# 设置模拟空间的大小
size = 80
center = size/2
space = np.zeros((size, size))

# 初始化模拟空间，放置一个种子
seed_x, seed_y = size // 2, size // 2
space[seed_x, seed_y] = 1

# 定义生长规则
def get_neighbors(x, y, space):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx != 0 or dy != 0) and 0 <= x + dx < space.shape[0] and 0 <= y + dy < space.shape[1]:
                if space[x + dx, y + dy] == 0:
                    neighbors.append((x + dx, y + dy))
    return neighbors

# 模拟生长过程
def grow(space, steps):
    Flag = True
    count = 0
    while Flag:
        # 获取所有已有细胞的坐标
        cells = np.argwhere(space == 1)
        # 随机选择一个已有的细胞
        cell = cells[random.randint(0, len(cells) - 1)]
        x, y = cell
        # 获取该细胞的空邻居
        neighbors = get_neighbors(x, y, space)
        if neighbors:
            # 随机选择一个邻居并在那里放置一个新细胞
            new_x, new_y = neighbors[random.randint(0, len(neighbors) - 1)]
            space[new_x, new_y] = 1
            count+=1
            if (count >=steps):
                Flag = False

# 运行生长模拟
grow(space, 2500)  # 运行5000步生长

# 可视化模拟结果
plt.figure(figsize=(10, 10))
plt.imshow(space, cmap='Greens', interpolation='nearest')
plt.title('Eden Growth Model')
plt.axis('off')
plt.show()

def calculate_mass(radius, space, center):
    """计算给定半径内的质量（被占据的位置数量）。"""
    y, x = np.ogrid[-center:size - center, -center:size - center]
    mask = x ** 2 + y ** 2 <= radius ** 2
    return np.sum(space[mask])


def fractal_dimension(space, center):
    """计算分形维数。"""
    radii = np.arange(1, center-20)
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