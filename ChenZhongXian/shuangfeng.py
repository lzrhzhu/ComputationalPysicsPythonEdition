import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

# 定义光强计算函数
def intensity(lamda, d, D, x):
    theta = np.arctan(x/D)
    phi = d * np.sin(theta) * 2 * np.pi / lamda
    return 2 * (1 + np.cos(phi))
# 创建x和y的网格
x = np.linspace(-0.01, 0.01, 1000)
y = np.linspace(-0.01, 0.01, 1000)
X, Y = np.meshgrid(x, y)

# 初始值
lamda = 632.8e-9
d = 2e-3
D = 1

# 计算光强
I = intensity(lamda, d, D, X)

# 创建干涉图
plt.imshow(I, cmap='gray', extent=[-0.01, 0.01, -0.01, 0.01])
plt.colorbar(label='Intensity')
plt.show()

# 创建滑块
lamda_slider = FloatSlider(min=400e-9, max=700e-9, step=10e-9, value=lamda, description='Lambda (m)')
d_slider = FloatSlider(min=1e-3, max=3e-3, step=0.1e-3, value=d, description='d (m)')

# 定义滑块的回调函数
def update(lamda, d):
    # 计算新的光强
    I = intensity(lamda, d, D, X)
    # 更新图
    plt.imshow(I, cmap='gray', extent=[-0.01, 0.01, -0.01, 0.01])
    plt.colorbar(label='Intensity')
    plt.show()

# 使用交互式功能
interact(update, lamda=lamda_slider, d=d_slider);