import numpy as np
import matplotlib.pyplot as plt

def euler_cromer_method(t0, y0, t_end, dt, g, l, q):
    t_values = np.arange(t0, t_end+dt, dt)
    theta_values = [y0[0]]
    w_values = [y0[1]]

    for t in t_values[:-1]:
        theta = theta_values[-1]
        w = w_values[-1]

        w_new = w - (g/l) * theta * dt - q * w * dt
        theta_new = theta + dt * w_new

        theta_values.append(theta_new)
        w_values.append(w_new)

    return theta_values, t_values

def main():
    t0 = 0
    y0 = np.array([0.2, 0])
    t_end = 10
    dt = 0.01
    g = 9.8
    l = 1
    q_values = [1.0, 5.0, 10.0]

    for q in q_values:
        theta, t = euler_cromer_method(t0, y0, t_end, dt, g, l, q)
        plt.plot(t, theta, label=f'q = {q}')

    plt.xlabel('Time (s)')
    plt.ylabel('Theta (radians)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()