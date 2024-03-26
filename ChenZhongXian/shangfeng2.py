import numpy as np
import matplotlib.pyplot as plt

# 定义常数
wavelength = 500e-9  # 波长为500nm
D = 1  # 双缝到屏幕的距离为1m
d = 2e-3  # 双缝间距为2mm
x = np.linspace(-2e-3, 2e-3, 1000)  # 在x方向上均匀采样
y = np.linspace(-2e-3, 2e-3, 1000)  # 在y方向上均匀采样
X, Y = np.meshgrid(x, y)  # 生成网格点坐标矩阵

# 计算干涉条纹的亮度分布
intensity = (np.cos(np.pi * d * np.sin(np.arctan(X / D)) / wavelength))**2
brightness = intensity / np.max(intensity)  # 计算亮度分布

# 绘制亮度在xy平面内的分布图
plt.figure(figsize=(8, 6))
plt.contourf(X * 1e3, Y * 1e3, brightness, cmap='hot')
plt.colorbar(label='Brightness')
plt.xlabel('X (mm)')
plt.ylabel('Y (mm)')
plt.title('Double Slit Interference Brightness Distribution in XY Plane')
plt.show()