import numpy as np
import matplotlib.pyplot as plt

# 定义方程参数
tau = 1  # tau值为1秒
N0 = 100  # 初始N值为100

# 定义时间间隔和总时间
dt1 = 0.2  # 时间间隔为0.2秒
dt2 = 0.05  # 时间间隔为0.05秒
total_time = 10  # 总时间为10秒

# 计算时间步数
num_steps1 = int(total_time / dt1)
num_steps2 = int(total_time / dt2)

# 初始化时间和N值的数组
t1 = np.zeros(num_steps1+1)
t2 = np.zeros(num_steps2+1)
N1 = np.zeros(num_steps1+1)
N2 = np.zeros(num_steps2+1)
N_exact = np.zeros(num_steps1+1)

# 设置初始值
t1[0] = 0
t2[0] = 0
N1[0] = N0
N2[0] = N0
N_exact[0] = N0

# 使用欧拉一阶近似法计算N随时间变化的曲线（时间间隔为0.2秒）
for i in range(num_steps1):
    t1[i+1] = t1[i] + dt1
    N1[i+1] = N1[i] - (N1[i] / tau) * dt1

# 使用欧拉一阶近似法计算N随时间变化的曲线（时间间隔为0.05秒）
for i in range(num_steps2):
    t2[i+1] = t2[i] + dt2
    N2[i+1] = N2[i] - (N2[i] / tau) * dt2

# 使用解析解法计算N随时间变化的曲线
for i in range(num_steps1):
    N_exact[i+1] = N0 * np.exp(-t1[i+1] / tau)

# 使用matplotlib绘制N随时间变化的曲线
plt.plot(t1, N1, 'bo', markersize=4, label='Euler (dt=0.2s)')
plt.plot(t2, N2, 'v', markersize=4, label='Euler (dt=0.05s)')
plt.plot(t1, N_exact, 's', markersize=4, label='Exact Solution')
plt.xlabel('Time')
plt.ylabel('N')
plt.title('N vs Time')
plt.legend()
plt.show()