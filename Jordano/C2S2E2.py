import numpy as np
import matplotlib.pyplot as plt

# 定义常量
B2 = 4e-5
m = 1
g = 9.8

# 定义初始条件
v0 = 700  # 初始速度
theta1 = np.deg2rad(35)  # 发射角度为35度
theta2 = np.deg2rad(45)  # 发射角度为45度

# 定义时间步长和总时间
dt = 0.01
T = 10

# 定义求解函数
def solve_euler(v0, theta):
    # 初始化变量
    t = [0]
    x = [0]
    y = [0]
    vx = [v0 * np.cos(theta)]
    vy = [v0 * np.sin(theta)]

    # 迭代求解微分方程
    while y[-1] >= 0:
        t.append(t[-1] + dt)
        x.append(x[-1] + vx[-1] * dt)
        y.append(y[-1] + vy[-1] * dt)
        vx.append(vx[-1] - B2 * vx[-1] * np.sqrt(vx[-1]**2 + vy[-1]**2) / m * dt)
        vy.append(vy[-1] - g * dt - B2 * vy[-1] * np.sqrt(vx[-1]**2 + vy[-1]**2) / m * dt)

    return x, y

# 求解并绘制轨迹曲线
x1, y1 = solve_euler(v0, theta1)
x2, y2 = solve_euler(v0, theta2)

plt.plot(x1, y1, label='35 degrees')
plt.plot(x2, y2, label='45 degrees')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()