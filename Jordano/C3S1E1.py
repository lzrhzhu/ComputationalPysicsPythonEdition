import numpy as np
import matplotlib.pyplot as plt

def euler_method(t0, y0, t_end, dt, g, l):
    t_values = np.arange(t0, t_end+dt, dt)
    theta_values = [y0[0]]
    w_values = [y0[1]]

    for t in t_values[:-1]:
        theta = theta_values[-1]
        w = w_values[-1]

        theta_new = theta + dt * w
        w_new = w - (g/l) * np.sin(theta) * dt

        theta_values.append(theta_new)
        w_values.append(w_new)

    return theta_values, w_values

def euler_cromer_method(t0, y0, t_end, dt, g, l):
    t_values = np.arange(t0, t_end+dt, dt)
    theta_values = [y0[0]]
    w_values = [y0[1]]

    for t in t_values[:-1]:
        theta = theta_values[-1]
        w = w_values[-1]

        w_new = w - (g/l) * np.sin(theta) * dt
        theta_new = theta + dt * w_new

        theta_values.append(theta_new)
        w_values.append(w_new)

    return theta_values, w_values

def main():
    t0 = 0
    y0 = np.array([np.radians(5), 0])
    t_end = 10
    dt = 0.01
    g = 9.8
    l = 1

    # 使用Euler方法求解微分方程组
    theta_euler, w_euler = euler_method(t0, y0, t_end, dt, g, l)

    # 使用Euler-Cromer方法求解微分方程组
    theta_euler_cromer, w_euler_cromer = euler_cromer_method(t0, y0, t_end, dt, g, l)

    # 绘制图形
    t_values = np.arange(t0, t_end+dt, dt)
    plt.plot(t_values, theta_euler, label='Euler')
    plt.plot(t_values, theta_euler_cromer, label='Euler-Cromer')
    plt.xlabel('Time (s)')
    plt.ylabel('Theta (radians)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()