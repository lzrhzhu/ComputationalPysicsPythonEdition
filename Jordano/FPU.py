import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 初始化参数
N = 32  # 质点的数量
m = 1.0  # 质点的质量
k = 1.0  # 线性弹簧常数
beta = 0.01  # 非线性弹簧常数
t_max = 10000  # 模拟时间
dt = 0.05  # 时间步长
num_steps = int(t_max / dt)  # 时间步数

dt2 = dt*dt
# 初始化位置和速度
positions = np.zeros(shape=(N+2, num_steps), dtype=np.float64)

# 设置初始条件为模式1的振动模式，振幅为10
positions[1:N+2, 0] = 10 * np.sin(np.pi * np.arange(1, N+2) / (N + 1))
positions[1:N+2, 1] = positions[1:N+2, 0]  # 初始速度为零

# Verlet积分
for t in range(1, num_steps - 1):
    for i in range(1, N+1):  # 端点不动
        force = -k * (2 * positions[i, t] - positions[i - 1, t] - positions[i + 1, t]) \
                - beta * ((positions[i, t] - positions[i - 1, t]) ** 3 - (positions[i + 1, t] - positions[i, t]) ** 3)
        positions[i, t + 1] = 2 * positions[i, t] - positions[i, t - 1] + (force / m) * dt2

# 初始化能量数组
E1 = np.zeros(num_steps, dtype=np.float64)  # 3行对应模式1，3，5
E3 = np.zeros(num_steps, dtype=np.float64)  #
E5 = np.zeros(num_steps, dtype=np.float64)
Q1 = np.zeros(num_steps, dtype=np.float64)
Q3 = np.zeros(num_steps, dtype=np.float64)
Q5 = np.zeros(num_steps, dtype=np.float64)
QV1 = np.zeros(num_steps, dtype=np.float64)
QV3 = np.zeros(num_steps, dtype=np.float64)
QV5 = np.zeros(num_steps, dtype=np.float64)

w1 = 2 * np.sin(np.pi * 1/(2*N+2))
w3 = 2 * np.sin(np.pi * 3/(2*N+2))
w5 = 2 * np.sin(np.pi * 5/(2*N+2))
velocities = np.zeros((N+2, num_steps), dtype=np.float64)
# 计算能量
for i in range(1, num_steps-1):
    # 计算速度 (v = (x(t+dt) - x(t-dt)) / (2*dt))
    velocities[:, i] = (positions[:, i + 1] - positions[:, i - 1]) / (2 * dt)

for j in range(1, N+1):
    Q1[1: num_steps-1] += positions[j, 1: num_steps-1] * np.sin( 1 * np.pi * j /(N+1) )
    Q3[1: num_steps-1] += positions[j, 1: num_steps-1] * np.sin( 3 * np.pi * j /(N+1) )
    Q5[1: num_steps-1] += positions[j, 1: num_steps-1] * np.sin( 5 * np.pi * j /(N+1) )
    QV1[1: num_steps-1] += velocities[j, 1:num_steps-1] * np.sin(1 * np.pi * j/(N+1))
    QV3[1: num_steps-1] += velocities[j, 1:num_steps-1] * np.sin(3 * np.pi * j/(N+1))
    QV5[1: num_steps-1] += velocities[j, 1:num_steps-1] * np.sin(5 * np.pi * j/(N+1))

E1 = 0.5 * ( QV1 * QV1 + w1 * w1 *  Q1 * Q1)
E3 = 0.5 * ( QV3 * QV3 + w3 * w3 *  Q3 * Q3)
E5 = 0.5 * ( QV5 * QV5 + w5 * w5 *  Q5 * Q5)

# 创建动画
fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-', lw=2)
ax.set_xlim(0, N+2)
ax.set_ylim(-15, 15)
ax.set_xlabel('Particle Number')
ax.set_ylabel('Displacement')

def init():
    line.set_data([], [])
    return (line,)

def animate(t):
    x = np.arange(N+2)
    y = positions[:, t]
    line.set_data(x, y)
    return (line,)
ani = FuncAnimation(fig, animate, frames=num_steps, init_func=init, blit=True, interval=1)
plt.show()

# 绘制能量随时间的变化
plt.figure(figsize=(15, 5))
time = np.arange(0, num_steps) * dt
plt.plot(time[1:num_steps-1], E1[1:num_steps-1], label='Mode 1')
plt.plot(time[1:num_steps-1], E3[1:num_steps-1], label='Mode 3')
plt.plot(time[1:num_steps-1], E5[1:num_steps-1], label='Mode 5')

plt.xlabel('Time')
plt.ylabel('Energy')
plt.legend()
plt.title('Energy vs Time for Modes 1, 3, and 5')
plt.show()