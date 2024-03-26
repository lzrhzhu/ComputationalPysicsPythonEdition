import numpy as np
import matplotlib.pyplot as plt

# 定义常量
B2 = 4e-5
m = 1
g = 9.8
a = 6.5e-3
alpha = 2.5
T0 = 300  # 参考温度
rou0 = 1.225  # 参考空气密度

# 定义初始条件
v0 = 700  # 初始速度
theta1 = np.deg2rad(35)  # 发射角度为35度
theta2 = np.deg2rad(45)  # 发射角度为45度

# 定义时间步长和总时间
dt = 0.01
T = 10

# 定义求解函数
def solve_euler(v0, theta, density_effect=True):
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

        if density_effect:
            rou = (1 - a * y[-1] / T0) ** alpha
            vx.append(vx[-1] - B2 * rou / rou0 * vx[-1] * np.sqrt(vx[-1]**2 + vy[-1]**2) / m * dt)
            vy.append(vy[-1] - g * dt - B2 * rou / rou0 * vy[-1] * np.sqrt(vx[-1]**2 + vy[-1]**2) / m * dt)
        else:
            vx.append(vx[-1] - B2 * vx[-1] * np.sqrt(vx[-1]**2 + vy[-1]**2) / m * dt)
            vy.append(vy[-1] - g * dt - B2 * vy[-1] * np.sqrt(vx[-1]**2 + vy[-1]**2) / m * dt)

    return x, y

# 求解并绘制轨迹曲线
x1, y1 = solve_euler(v0, theta1, True)
x2, y2 = solve_euler(v0, theta2, True)
x3, y3 = solve_euler(v0, theta1, False)
x4, y4 = solve_euler(v0, theta2, False)

# 将单位转换为千米
x1 = np.array(x1) / 1000
y1 = np.array(y1) / 1000
x2 = np.array(x2) / 1000
y2 = np.array(y2) / 1000
x3 = np.array(x3) / 1000
y3 = np.array(y3) / 1000
x4 = np.array(x4) / 1000
y4 = np.array(y4) / 1000

# 设置坐标轴范围
plt.xlim(0, 30)
plt.ylim(0, 10)

plt.plot(x1, y1, label='35 degrees with density effect')
plt.plot(x2, y2, label='45 degrees with density effect')
plt.plot(x3, y3, label='35 degrees without density effect')
plt.plot(x4, y4, label='45 degrees without density effect')
plt.xlabel('x (km)')
plt.ylabel('y (km)')
plt.legend()
plt.show()