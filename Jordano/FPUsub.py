import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# 参数设定
N = 32          # 质点个数
k = 1.0         # 弹簧常数
beta = 0.3      # 非线性系数
A = 1.0         # 振幅
dt = 0.05       # 时间间隔
total_time = 100 # 总模拟时间
num_steps = int(total_time / dt)

# 初始化位置和速度
x = np.zeros((N+2, num_steps+1))
v = np.zeros((N+2, num_steps+1))

# 设置初始位置为频率最低的驻波模式
for i in range(1, N+1):
    x[i, 0] = A * np.sqrt(2.0 / (N + 1)) * np.sin(np.pi * i / (N + 1))
x[:,1] = x[:,0]

# 使用Verlet积分更新位置
for t in range(2, num_steps):
    for i in range(1, N+1):
        F_linear = -k * (2 * x[i, t-1] - x[i-1, t-1] - x[i+1, t-1])
        F_nonlinear = -beta * ((x[i, t-1] - x[i-1, t-1])**3 - (x[i+1, t-1] - x[i, t-1])**3)
        F_total = F_linear + F_nonlinear
        x[i, t+1] = 2 * x[i, t-1] - x[i, t-2] + (F_total * dt**2)

# 计算傅里叶变换
ak = np.zeros((N+1, num_steps+1))
for k in range(1, N+1):
    for t in range(num_steps+1):
        ak[k, t] = np.sqrt(2.0 / (N + 1)) * np.sum(x[1:N+1, t] * np.sin(np.arange(1, N+1) * k * np.pi / (N + 1)))

# 计算动能
Ek = np.zeros((N+1, num_steps-1))
for k in range(1, N+1):
    wk = 2 * np.sin(k * np.pi / (2 * (N + 1)))
    for t in range(1, num_steps-1):
        ak_dot = (ak[k, t] - ak[k, t-1]) / dt
        Ek[k, t] = 0.5 * (ak_dot**2 + wk**2 * ak[k, t]**2)

# 绘制Ek随时间的变化
modes_to_plot = [1, 3, 5]


for mode in modes_to_plot:
    plt.plot(np.arange(num_steps-1) * dt, Ek[mode, :num_steps], label=f'Mode {mode}')

plt.xlabel('Time')
plt.ylabel('Energy')
plt.title('Energy of Modes over Time')
plt.legend()
plt.show()