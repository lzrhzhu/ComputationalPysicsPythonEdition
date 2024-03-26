import numpy as np
import matplotlib.pyplot as plt

# 初始化参数
box_length = 20.0
epsilon = 1.0
sigma = 1.0
mass = 1.0
dt = 0.01
num_atoms = 144  # 假设我们有100个原子
num_steps = 200  # 我们只模拟到60个时间点

# 初始化原子位置为二维格点
num_per_side = int(np.sqrt(num_atoms))
assert num_per_side**2 == num_atoms, "num_atoms must be a perfect square for a 2D square lattice."

lattice_spacing = box_length / num_per_side
x = np.linspace(0, box_length - lattice_spacing, num_per_side)
y = np.linspace(0, box_length - lattice_spacing, num_per_side)
xx, yy = np.meshgrid(x, y)
positions = np.vstack([xx.ravel(), yy.ravel()]).T

# 初始化速度为大小为1，方向随机
angles = 2 * np.pi * np.random.rand(num_atoms)
velocities = np.vstack([np.cos(angles), np.sin(angles)]).T

accelerations = np.zeros((num_atoms, 2))

# 周期性边界条件下的最小图像约定
def minimum_image_distance(r_vec, box_length):
    return r_vec - box_length * np.round(r_vec / box_length)

# 计算Lennard-Jones力，考虑周期性边界条件
def compute_forces(pos, box_length):
    forces = np.zeros((num_atoms, 2))
    for i in range(num_atoms):
        for j in range(i + 1, num_atoms):
            r_vec = pos[i] - pos[j]
            r_vec = minimum_image_distance(r_vec, box_length)
            r = np.linalg.norm(r_vec)
            r6 = (sigma / r) ** 6
            r12 = r6 ** 2
            f_mag = 24 * epsilon * (2 * r12 - r6) / (r ** 2)
            f_vec = f_mag * r_vec
            forces[i] += f_vec
            forces[j] -= f_vec
    return forces

# Verlet积分法更新位置和速度
def verlet_integrate(pos, vel, acc, box_length):
    new_pos = pos + vel * dt + 0.5 * acc * dt ** 2
    # 对新位置应用周期性边界条件
    new_pos = new_pos % box_length
    new_forces = compute_forces(new_pos, box_length)
    new_acc = new_forces / mass
    new_vel = vel + 0.5 * (acc + new_acc) * dt
    return new_pos, new_vel, new_acc

# 用于存储不同时间段速度的列表
speeds_0_20 = []
speeds_20_40 = []
speeds_40_60 = []
speeds_180_200 = []

# 运行模拟并收集数据
for step in range(num_steps):
    positions, velocities, accelerations = verlet_integrate(positions, velocities, accelerations, box_length)

    # 收集不同时间段的速度
    if 1 <= step < 20:
        speeds_0_20.extend(np.linalg.norm(velocities, axis=1))
    elif 20 <= step < 40:
        speeds_20_40.extend(np.linalg.norm(velocities, axis=1))
    elif 40 <= step < 60:
        speeds_40_60.extend(np.linalg.norm(velocities, axis=1))
    elif 180 <= step < 200:
        speeds_180_200.extend(np.linalg.norm(velocities, axis=1))

# 绘制速度分布
plt.figure(figsize=(10, 6))

# 0-20 时间点的速度统计分布
#hist_0_20, bins_0_20 = np.histogram(speeds_0_20, bins=20, density=True)
#plt.plot(bins_0_20[:-1], hist_0_20, label='0-20 time points', color='blue')

# 20-40 时间点的速度统计分布
hist_20_40, bins_20_40 = np.histogram(speeds_20_40, bins=20, density=True)
plt.plot(bins_20_40[:-1], hist_20_40, label='20-40 time points', linestyle='dashed', color='green')

# 40-60 时间点的速度统计分布
hist_40_60, bins_40_60 = np.histogram(speeds_40_60, bins=20, density=True)
plt.plot(bins_40_60[:-1], hist_40_60, label='40-60 time points', linestyle='dashdot', color='red')

# 180—200
hist_180_200, bins_180_200 = np.histogram(speeds_40_60, bins=20, density=True)
plt.plot(bins_180_200[:-1], hist_180_200, label='180-200 time points', linestyle='dashdot', color='blue')

plt.xlabel('Speed (arbitrary units)')
plt.ylabel('Probability Density')
plt.title('Speed Distribution')
plt.legend()
plt.show()