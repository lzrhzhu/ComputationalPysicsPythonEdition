import numpy as np
import matplotlib.pyplot as plt

# 定义欧拉-克罗默方法
def euler_cromer_method(t0, y0, t_end, dt, g, l, q, WD, FD):
    t_values = np.arange(t0, t_end+dt, dt)
    theta_values = [y0[0]]
    w_values = [y0[1]]

    for t in t_values[:-1]:
        theta = theta_values[-1]
        w = w_values[-1]

        w_new = w - (g/l) * theta * dt - q * w * dt + FD * np.sin(WD * t) * dt
        theta_new = theta + dt * w_new

        theta_values.append(theta_new)
        w_values.append(w_new)

    return theta_values, t_values

# (1) q = 1.0， Wd = 2.0 FD=0.2  初始  theta = 0.2，   时间范围 0 到 20
q = 1.0
WD = 2.0
FD = 0.2
y0_1 = np.array([0.2, 0])
t0 = 0
t_end = 20
dt = 0.01
g = 9.8
l = 1.0

theta_values_1, t_values_1 = euler_cromer_method(t0, y0_1, t_end, dt, g, l, q, WD, FD)

plt.figure()
plt.plot(t_values_1, theta_values_1)
plt.xlabel('Time (s)')
plt.ylabel('Theta (radians)')
plt.title('q = 1.0, WD = 2.0, FD = 0.2')
plt.show()

