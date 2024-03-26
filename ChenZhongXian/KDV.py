import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 初始参数
L = 50.0
T = 100.0
dx = 0.1
dt = 0.01
x = np.arange(0, L, dx)
N = len(x)
t = np.arange(0, T, dt)
c = 0.2

# 初始条件
init = np.sin(np.pi*x)

# KdV方程的求解
def kdv(u, dx, dt, c):
    u_xx = (np.roll(u, -1) - 2*u + np.roll(u, 1)) / dx**2
    u_xxx = (np.roll(u, -2) - 2*np.roll(u, -1) + 2*np.roll(u, 1) - np.roll(u, 2)) / (2*dx**3)
    u_t = -c*u*u_xx - u_xxx
    return u_t

# 时间积分
def time_step(u, dx, dt, c):
    k1 = kdv(u, dx, dt, c)
    k2 = kdv(u + k1*dt/2, dx, dt, c)
    k3 = kdv(u + k2*dt/2, dx, dt, c)
    k4 = kdv(u + k3*dt, dx, dt, c)
    return u + dt/6*(k1 + 2*k2 + 2*k3 + k4)

sol = []
u = init
for _ in t:
    u = time_step(u, dx, dt, c)
    sol.append(u)

# 可视化
fig, ax = plt.subplots()
line, = ax.plot(x, sol[0])

def animate(i):
    line.set_ydata(sol[i])
    return line,

ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=50, blit=True)

plt.show()