import numpy as np
import matplotlib.pyplot as plt

m = 70  # 质量（kg）
P = 400  # 功率（W）
A = 0.33  # 横截面积（m^2）
C = 0.5  # 阻力系数
rou = 1.1691  # 空气密度（kg/m^3）
v0 = 4  # 初始速度（m/s）
t0 = 0  # 初始时间（s）
t_end = 200  # 结束时间（s）
dt = 0.1  # 时间步长（s）

num_steps = int((t_end - t0) / dt)  # 时间步数
t = np.zeros(num_steps+1)  # 时间数组
v = np.zeros(num_steps+1)  # 速度数组
t[0] = t0  # 初始时间
v[0] = v0  # 初始速度

for i in range(num_steps):
    t[i+1] = t[i] + dt  # 更新时间
    F = (P / v[i]) - (0.5 * rou * A * v[i]**2)  # 计算力F
    v[i+1] = v[i] + (F / m) * dt  # 更新速度

rou = 0  # 空气密度（kg/m^3）
v_no_air_resistance = np.zeros(num_steps+1)  # 没有空气阻力的速度数组
v_no_air_resistance[0] = v0  # 初始速度

for i in range(num_steps):
    F_no_air_resistance = P / v_no_air_resistance[i]  # 计算力F（没有空气阻力）
    v_no_air_resistance[i+1] = v_no_air_resistance[i] + (F_no_air_resistance / m) * dt  # 更新速度（没有空气阻力）

plt.plot(t, v, 'b-', label='With Air Resistance')
plt.plot(t, v_no_air_resistance, 'r--', label='No Air Resistance')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time')
plt.legend()
plt.show()