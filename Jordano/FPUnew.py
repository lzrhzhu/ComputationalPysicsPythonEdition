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
save_span = 20  # 存储的时间
num_steps = int(t_max / dt)  # 时间步数
dt2 = dt*dt
w1 = 2 * np.sin(np.pi * 1/(2*N+2))
w3 = 2 * np.sin(np.pi * 3/(2*N+2))
w5 = 2 * np.sin(np.pi * 5/(2*N+2))
# 初始化位置和速度
positions_old = np.zeros(shape=(N+2), dtype=np.float64)
positions_now = np.zeros(shape=(N+2), dtype=np.float64)
positions_new = np.zeros(shape=(N+2), dtype=np.float64)
velocities_now = np.zeros(shape=(N+2), dtype=np.float64)
position_save = []
velocities_save = []
E1_save = []
E3_save = []
E5_save = []
# 设置初始条件为模式1的振动模式，振幅为10
positions_old[1:N+2] = 10 * np.sin(np.pi * np.arange(1, N+2) / (N + 1))
positions_now[1:N+2] = positions_old[1:N+2]  # 初始速度为零

# Verlet积分
for count in range(1, num_steps - 1):
    for i in range(1, N+1):  # 端点不动
        force = -k * (2 * positions_now[i] - positions_now[i-1] - positions_now[i + 1]) \
                - beta*( (positions_now[i] - positions_now[i-1])**3-(positions_now[i + 1]-positions_now[i])**3 )
        positions_new[i] = 2 * positions_now[i] - positions_old[i] + (force / m) * dt2
    if(  count % save_span ==0):
        velocities_now = (positions_new[:] - positions_old[:]) / (2 * dt)
        position_save.append( positions_now)
        velocities_save.append( velocities_now)
        Q1, Q3, Q5, QV1, QV3, QV5, = 0, 0, 0, 0, 0, 0
        for j in range(1, N + 1):
            Q1 += positions_now[j] * np.sin(1 * np.pi * j / (N + 1))
            Q3 += positions_now[j] * np.sin(3 * np.pi * j / (N + 1))
            Q5 += positions_now[j] * np.sin(5 * np.pi * j / (N + 1))
            QV1 += velocities_now[j] * np.sin(1 * np.pi * j / (N + 1))
            QV3 += velocities_now[j] * np.sin(3 * np.pi * j / (N + 1))
            QV5 += velocities_now[j] * np.sin(5 * np.pi * j / (N + 1))
        E1 = 0.5 * (QV1 * QV1 + w1 * w1 * Q1 * Q1)
        E3 = 0.5 * (QV3 * QV3 + w3 * w3 * Q3 * Q3)
        E5 = 0.5 * (QV5 * QV5 + w5 * w5 * Q5 * Q5)
        E1_save.append(E1)
        E3_save.append(E3)
        E5_save.append(E5)
    positions_now[:] = positions_new[:]
    positions_old[:] = positions_now[:]

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
    print("  position_save = ", position_save.__sizeof__())
    y = np.zeros(shape=(N+2, position_save.__sizeof__()), dtype=np.float64)
    for count in range(0,   position_save.__sizeof__()):
        y[:,count]= position_save[count]

    line.set_data(x, y)
    return (line,)
ani = FuncAnimation(fig, animate, frames=num_steps, init_func=init, blit=True, interval=1)
plt.show()

# 绘制能量随时间的变化
plt.figure(figsize=(15, 5))
time = np.arange(0, E1_save.__sizeof__()) * dt * save_span
plt.plot(time, E1_save, label='Mode 1')
plt.plot(time, E3_save, label='Mode 3')
plt.plot(time, E5_save, label='Mode 5')

plt.xlabel('Time')
plt.ylabel('Energy')
plt.legend()
plt.title('Energy vs Time for Modes 1, 3, and 5')
plt.show()