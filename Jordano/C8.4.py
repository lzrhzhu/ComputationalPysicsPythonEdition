import numpy as np
import matplotlib.pyplot as plt

# 玻尔兹曼常数
kB = 1.0

# 初始化自旋，所有自旋朝向1方向
L = 10  # 方形格子的边长
spins = np.ones((L, L), dtype=int)

# 定义翻转能量计算函数
def calculate_energy_flip(spins, i, j, H):
    S = spins[i, j]
    # 周期性边界条件
    nb = spins[(i+1)%L, j] + spins[i, (j+1)%L] + spins[(i-1)%L, j] + spins[i, (j-1)%L]
    Eflip = 2 * S * (nb + H)
    return Eflip

# 定义磁化计算函数
def calculate_magnetization(spins):
    mag = np.sum(spins)
    return mag / (L**2)  # 归一化磁化

# 蒙特卡洛扫描
def monte_carlo_simulation(T, H=0.0, num_steps=1000):
    magnetizations = []
    for step in range(num_steps):
        for _ in range(L**2):
            i, j = np.random.randint(0, L, size=2)
            Eflip = calculate_energy_flip(spins, i, j, H)
            if Eflip < 0 or np.random.rand() < np.exp(-Eflip / (kB * T)):
                spins[i, j] *= -1  # 反转自旋
        magnetizations.append(calculate_magnetization(spins))
    return magnetizations

# 温度列表
temperatures = [1.5, 2.0, 2.25, 4.0]

# 绘图
plt.figure(figsize=(14, 7))

for T in temperatures:
    magnetizations = monte_carlo_simulation(T)
    plt.plot(magnetizations, label=f'T={T}')

plt.xlabel('Monte Carlo Steps')
plt.ylabel('Absolute Magnetization')
plt.ylim(-0.5, 1.5)
plt.legend()
plt.tight_layout()
plt.show()