import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 定义参数
N = 100  # x方向上的网格数量
M = 100  # y方向上的网格数量
P = 100  # 时间步长数量
l = 1.0  # x方向上的长度
s = 1.0  # y方向上的长度
T = 1.0  # 总时间
lamda = 1.0  # 热传导系数

# 离散化参数
dx = l / N
dy = s / M
dt = T / P

# 初始化温度分布
u = np.zeros((N+1, M+1, P+1))

# 设置初始条件
u[:, :, 0] = 0.0  # 在t=0时刻的温度分布

# 设置边界条件
u[0, :, :] = 0.0  # x=0边界
u[N, :, :] = 1.0  # x=l边界
u[:, 0, :] = 0.0  # y=0边界
u[:, M, :] = 0.0  # y=s边界

# 创建动画图像
fig = plt.figure()
ax = plt.axes(xlim=(0, l), ylim=(0, s))
heatmap = ax.imshow(u[:, :, 0], cmap='hot', interpolation='nearest', origin='lower')

# 更新温度分布
def update(frame):
    for i in range(1, N):
        for j in range(1, M):
            u[i, j, frame+1] = u[i, j, frame] + lamda * dt * ((u[i+1, j, frame] - 2*u[i, j, frame] + u[i-1, j, frame]) / dx**2 + (u[i, j+1, frame] - 2*u[i, j, frame] + u[i, j-1, frame]) / dy**2)
    heatmap.set_array(u[:, :, frame+1])

# 创建动画
animation = FuncAnimation(fig, update, frames=P, interval=50, repeat=False)

# 显示动画
plt.show()