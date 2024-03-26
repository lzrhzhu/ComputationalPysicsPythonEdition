import math
import matplotlib.pyplot as plt
def euler_method(dt, x0, y0, vx0, vy0, theta):
    g = 9.8  # 重力加速度
    t = 0.0  # 时间
    x = x0  # 初始x坐标
    y = y0  # 初始y坐标
    vx = vx0 * math.cos(math.radians(theta))  # 初始x方向速度
    vy = vy0 * math.sin(math.radians(theta))  # 初始y方向速度

    x_values = [x]  # 存储x坐标的列表
    y_values = [y]  # 存储y坐标的列表

    while y >= 0:
        x += vx * dt
        y += vy * dt
        vy -= g * dt

        x_values.append(x)
        y_values.append(y)

        t += dt

    return x_values, y_values


# 初始条件
x0 = 0
y0 = 0
v0 = 700

# 不同角度
theta_values = [30, 35, 40, 45, 50, 55]

# 时间步长
dt = 0.01

# 绘制轨迹图
plt.figure(figsize=(10, 6))
plt.xlabel('x')
plt.ylabel('y')

for theta in theta_values:
    x_values, y_values = euler_method(dt, x0, y0, v0, v0, theta)
    plt.plot(x_values, y_values, label=f'theta = {theta} degrees')

plt.legend()
plt.title('Projectile Motion')
plt.show()