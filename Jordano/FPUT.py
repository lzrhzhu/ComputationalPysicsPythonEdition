import matplotlib as plt
import numpy as np
N = 31
dt = 1
ddt = 0.01 #步长0.01
totalt = 1000000; #步数1000000
alpha = 0.25;
beta = 0; #只计算到2阶
omega = np.zeros(N + 2,1);
psi  = np.zeros(N + 2, N + 2);
xx   = np.zeros(N + 2, totalt);
vv   = np.zeros(N + 2, totalt);
aa  = np.zeros(N + 2, totalt);
#%第一个时刻：初始化
for ii in range(2, N + 1):
    omega[ii] = 2 * np.sin((ii - 1) * np.pi / (2 * (N + 1)))
    xx[ii, 1] = np.sin((ii - 1) * np.pi / 32)
    vv[ii, 1] = 0

for ii in range(2,N + 1):
    for jj in range(2,N + 1):
        psi[ii, jj] = np.sqrt(2 / (N + 1)) * np.sin((ii - 1) * (jj - 1) * np.pi / (N + 1));
#用牛顿运动定律，粗略算出第二个时刻的位置、速度
for ii in range(2, N + 1):
    aa[ii, 1] = (xx(ii + 1, 1) + xx(ii - 1, 1) - 2 * xx(ii, 1)) + alpha * (
            (xx(ii + 1, 1) - xx(ii, 1)) ^ 2 - (xx(ii, 1) - xx(ii - 1, 1)) ^ 2) + beta * (
                        (xx(ii + 1, 1) - xx(ii, 1)) ^ 3 - (xx(ii, 1) - xx(ii - 1, 1)) ^ 3);
    xx[ii, 2 * dt] = xx(ii, 1) + vv(ii, 1) * ddt + 0.5 * aa(ii, 1) * ddt ^ 2;
    vv[ii, 2 * dt] = vv(ii, 1) + aa(ii, 1) * ddt;
# verlet算法，用前两个时刻的位置算出第三个时刻的位置，以此类推，算出所有时刻的位置、速度、加速度
for count in range(2, totalt):
    t
for ii in range(2,N + 1):
    aa[ii, t] = (xx(ii + 1, t) + xx(ii - 1, t) - 2 * xx(ii, t)) + alpha * (
            (xx(ii + 1, t) - xx(ii, t)) ^ 2 - (xx(ii, t) - xx(ii - 1, t)) ^ 2) + beta * (
                        (xx(ii + 1, t) - xx(ii, t)) ^ 3 - (xx(ii, t) - xx(ii - 1, t)) ^ 3)
    xx(ii, t + dt) = 2 * xx(ii, t) - xx(ii, t - dt) + aa(ii, t) * ddt ^ 2
    vv(ii, t) = (xx(ii, t + dt) - xx(ii, t - dt)) / (2 * ddt)


ii = 1:N + 2;
# h = plot(ii, xx(:, 34));
    qq = np.zeros(1, N + 2)
    pp = np.zeros(1, N + 2)
    energy = np.zeros(N + 2, totalt)
    sum_energy = np.zeros(totalt, 1)

for t in range(1*dt, totalt*dt, dt):
    qq = psi * xx[:, t] #将普通坐标变换为简正坐标
    pp = psi * vv[:, t]
    energy[:, t]=0.5 * (pp. * pp + omega. * omega. * qq. * qq);

#取前五个简正模式，绘图
plt.plot(1: dt:totalt, energy(1: 5,:))