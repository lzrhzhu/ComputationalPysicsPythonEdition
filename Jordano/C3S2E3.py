import numpy as np
import matplotlib.pyplot as plt

# 定义欧拉-克罗默方法
def euler_cromer_method(t0, y0, t_end, dt, g, l, q):
    t_values = np.arange(t0, t_end+dt, dt)
    theta_values = [y0[0]]
    w_values = [y0[1]]

    for t in t_values[:-1]:
        theta = theta_values[-1]
        w = w_values[-1]

        w_new = w - (g/l) * np.sin(theta) * dt - q * w * dt
        theta_new = theta + dt * w_new

        theta_values.append(theta_new)
        w_values.append(w_new)

    return theta_values, t_values

# 参数设置
q = 0
t0 = 0
t_end = 10
dt = 0.01
g = 9.8
l = 1.0

# 初值 theta = 1.8
y0_1 = np.array([1.8, 0])
theta_values_1, t_values_1 = euler_cromer_method(t0, y0_1, t_end, dt, g, l, q)

# 初值 theta = 2.8
y0_2 = np.array([2.8, 0])
theta_values_2, t_values_2 = euler_cromer_method(t0, y0_2, t_end, dt, g, l, q)

# 绘制图形
plt.figure()
plt.plot(t_values_1, theta_values_1, label='theta = 1.8')
plt.plot(t_values_2, theta_values_2, label='theta = 2.8')
plt.xlabel('Time (s)')
plt.ylabel('Theta (radians)')
plt.title('q = 0')
plt.legend()

plt.show()