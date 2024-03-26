import numpy as np
from scipy.linalg import eigh
import matplotlib.pyplot as plt

def kapa(G, ra, epsilon_a, epsilon_b, f):
    G_norm = np.linalg.norm(G)
    if G_norm == 0:
        return 0
    else:
        return 3 * f * (1/epsilon_a - 1/epsilon_b) * (
            np.sin(G_norm * ra) / (G_norm * ra)**3 -
            np.cos(G_norm * ra) / (G_norm * ra)**2
        )

def construct_matrix(k, G_vectors, epsilon_inv_fourier, N_G):
    H = np.zeros((N_G, N_G), dtype=complex)
    for i in range(N_G):
        for j in range(N_G):
            G_diff = G_vectors[i] - G_vectors[j]
            H[i, j] = np.dot(k + G_vectors[i], k + G_vectors[j]) * epsilon_inv_fourier(G_diff)
    return H

# 参数
a = 1.0  # FCC晶格常数
ra = a / np.sqrt(8)  # 电介质球的半径
epsilon_a = 12  # 电介质球的介电系数
epsilon_b = 1  # 空气的介电系数
f = np.pi / (3 * np.sqrt(2))  # FCC晶格的填充因子

N_G = 15  # 平面波数量
G_max = N_G // 2  # 倒格子向量的最大值

# 生成BCC倒格子向量
b = 4 * np.pi / np.sqrt(3) / a
G_vectors = np.array(np.meshgrid(range(-G_max, G_max+1),
                                 range(-G_max, G_max+1),
                                 range(-G_max, G_max+1))).T.reshape(-1, 3) * b

# 计算带结构
k_points = [np.array([0, 0, 0]),  # Gamma点
            np.array([0.5, 0.5, 0.5]) * b,  # L点
            np.array([1, 0, 0]) * b,  # X点
            np.array([0, 0, 0])]  # Gamma点

k_path = np.array([np.linspace(k_points[i], k_points[i+1], 20, endpoint=False)
                   for i in range(len(k_points)-1)]).reshape(-1, 3)

band_structure = []
for k in k_path:
    H = construct_matrix(k, G_vectors, lambda G: kapa(G, ra, epsilon_a, epsilon_b, f), N_G)
    eigenvalues, eigenvectors = eigh(H)
    band_structure.append(np.sqrt(np.abs(eigenvalues.real)))  # 取平方根得到频率

# 绘制带结构
band_structure = np.array(band_structure).T
for band in band_structure:
    plt.plot(band)
plt.xlabel('k index')
plt.ylabel('Frequency (arbitrary units)')
plt.title('Photonic Crystal Band Structure')
plt.show()

