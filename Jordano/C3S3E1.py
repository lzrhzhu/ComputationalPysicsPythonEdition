import numpy as np
import matplotlib.pyplot as plt

# 定义欧拉-克罗默方法
def euler_cromer_method(t0, y0, t_end, dt, g, l, q, FD, WD):
    t_values = np.arange(t0, t_end+dt, dt)
    theta_values = [y0[0]]
    w_values = [y0[1]]

    for t in t_values[:-1]:
        theta = theta_values[-1]
        w = w_values[-1]

        w_new = w - (g/l) * np.sin(theta) * dt - q * w * dt + FD * np.sin(WD * t) * dt
        theta_new = theta + dt * w_new

        theta_values.append(theta_new)
        w_values.append(w_new)

    return theta_values, t_values

# 参数设置
q = 0.5
t0 = 0
t_end = 60
dt = 0.01
g = 9.8
l = 9.8
WD = 2.0/3.0

# 初值 theta = 0.2, omega = 0
y0 = np.array([0.2, 0])

# 绘制图形
plt.figure()

# FD = 0
FD = 0
theta_values, t_values = euler_cromer_method(t0, y0, t_end, dt, g, l, q, FD, WD)
plt.plot(t_values, theta_values, label='FD = 0')

# FD = 0.5
FD = 0.5
theta_values, t_values = euler_cromer_method(t0, y0, t_end, dt, g, l, q, FD, WD)
plt.plot(t_values, theta_values, label='FD = 0.5')

# FD = 1.2
FD = 1.2
theta_values, t_values = euler_cromer_method(t0, y0, t_end, dt, g, l, q, FD, WD)
plt.plot(t_values, theta_values, label='FD = 1.2')

plt.xlabel('Time (s)')
plt.ylabel('Theta (radians)')
plt.title('q = 0.5, g = 9.8, l = 9.8, WD = 2.0/3.0')
plt.legend()

plt.show()