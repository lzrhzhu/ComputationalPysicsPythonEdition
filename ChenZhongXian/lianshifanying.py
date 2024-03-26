import random
import numpy as np
import matplotlib.pyplot as plt

# 生成新的随机位置
def new_position(x, y, z, mean_free_path):
    theta = 2 * np.pi * random.random()
    phi = np.arccos(2 * random.random() - 1)
    r = random.expovariate(1/mean_free_path)
    x += r * np.sin(phi) * np.cos(theta)
    y += r * np.sin(phi) * np.sin(theta)
    z += r * np.cos(phi)
    return x, y, z

# 模拟链式反应
def simulate_chain_reaction(size, initial_atoms, mean_free_path):
    atoms = initial_atoms
    history = [atoms]
    while atoms > 0:
        new_atoms = 0
        for _ in range(atoms):
            x, y, z = (random.uniform(0, size) for _ in range(3))
            x, y, z = new_position(x, y, z, mean_free_path)
            # 判断新位置是否在铀块内
            if 0 <= x <= size and 0 <= y <= size and 0 <= z <= size:
                new_atoms += 2  # 每个裂变事件产生2个新的中子
        atoms = new_atoms
        history.append(atoms)
    return history

# 测试
size = 11  # 铀块的边长
initial_atoms = 100  # 初始原子数
mean_free_path = 6  # 中子的平均自由程

history = simulate_chain_reaction(size, initial_atoms, mean_free_path)
plt.plot(history)
plt.xlabel("Generation")
plt.ylabel("Number of Atoms")
plt.show()