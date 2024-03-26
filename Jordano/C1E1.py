import numpy as np
import matplotlib.pyplot as plt

# 定义方程参数
tau = 1  # tau值为1秒
N0 = 100  # 初始N值为100

# 定义时间间隔和总时间
dt = 0.05  # 时间间隔为0.05秒
total_time = 10  # 总时间为10秒

# 计算时间步数
num_steps = int(total_time / dt)

# 初始化时间和N值的数组
t = np.zeros(num_steps+1)
N = np.zeros(num_steps+1)

# 设置初始值
t[0] = 0
N[0] = N0

# 使用欧拉一阶近似法计算N随时间变化的曲线
for i in range(num_steps):
    t[i+1] = t[i] + dt
    N[i+1] = N[i] - (N[i] / tau) * dt

# 使用matplotlib绘制N随时间变化的曲线
plt.plot(t, N)
plt.xlabel('Time')
plt.ylabel('N')
plt.title('N vs Time')
plt.show()