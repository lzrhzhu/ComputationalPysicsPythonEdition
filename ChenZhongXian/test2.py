from vectorplot import *
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
line_global,  = ax_global.plot(x, y, linewidth=line_width_global)
ax_global.set_xlabel('x', fontsize=font_size_global)
ax_global.set_ylabel('y', fontsize=font_size_global)
plt.show()