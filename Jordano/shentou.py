import numpy as np
from scipy.ndimage import label

# 设置晶格的大小
n = 100  # 晶格的尺寸为 n x n
p = 0.6  # 每个格子被填充的概率

# 生成随机晶格
grid = np.random.rand(n, n) < p

# 标记连通区域
labeled_grid, num_features = label(grid)

# 检查是否有渗透
# 创建一个数组来标记顶部和底部的连通区域
top_labels = labeled_grid[0, :]
bottom_labels = labeled_grid[-1, :]

# 判断顶部和底部是否有相同的标签，如果有，则表示有渗透
percolates = np.any(np.isin(top_labels[top_labels > 0], bottom_labels))

print("Grid percolates:" if percolates else "Grid does not percolate")

# 可选：使用matplotlib来可视化晶格
import matplotlib.pyplot as plt

plt.imshow(labeled_grid, cmap='viridis')
plt.colorbar()
plt.title('Percolation Simulation')
plt.show()