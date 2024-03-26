import numpy as np
import matplotlib.pyplot as plt

# 定义相关的物理参数
R = 1.0  # 曲率半径
lamda = 598.3e-9  # 波长

# 定义x, y的范围
x = np.linspace(-0.008, 0.008, 1600)
y = np.linspace(-0.008, 0.008, 1600)
x, y = np.meshgrid(x, y)

# 计算r的值
r = np.sqrt(x**2 + y**2)

# 计算空气薄层的厚度
d = r ** 2 / (2 * R)

# 计算相位差
theta = 2 * np.pi * d / lamda + np.pi

# 计算光强
Intensity = 2 + 2 * np.cos(theta)

# 绘制图形
plt.imshow(Intensity, cmap='gray', extent=(-10, 10, -10, 10))
plt.colorbar(label='Intensity')
plt.show()