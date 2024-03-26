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
def monte_carlo_simulation(T, H=0.0, num_steps=1000, equilibration_steps=100):
    magnetizations = []
    for step in range(num_steps):
        for _ in range(L**2):
            i, j = np.random.randint(0, L, size=2)
            Eflip = calculate_energy_flip(spins, i, j, H)
            if Eflip < 0 or np.random.rand() < np.exp(-Eflip / (kB * T)):
                spins[i, j] *= -1  # 反转自旋

        # 等待系统平衡
        if step >= equilibration_steps:
            magnetizations.append(calculate_magnetization(spins))
    return np.mean(magnetizations)

# 设置温度范围
temperatures = np.arange(1.0, 4.2, 0.2)
magnetization_means = []

# 对每个温度计算磁化的平均绝对值
for T in temperatures:
    mag_mean = monte_carlo_simulation(T)
    magnetization_means.append(mag_mean)

# 绘图
plt.plot(temperatures, magnetization_means, marker='o')
plt.xlabel('Temperature (T)')
plt.ylabel('Average Magnetization (|M|)')
plt.title('Average Magnetization vs Temperature')
plt.grid(True)
plt.show()