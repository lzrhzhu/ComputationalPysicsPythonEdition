import matplotlib.pyplot as plt
from matplotlib import rcParams

# 初始化全局变量
aspect_ratio_global = 1.0
font_size_global = 12
line_width_global = 2
fig_global, ax_global = plt.subplots(figsize=(6*aspect_ratio_global, 6))

# 定义全局函数
def on_resize_global(event):
    width_inches = event.width / fig_global.dpi
    height_inches = event.height / fig_global.dpi
    if width_inches / height_inches > aspect_ratio_global:
        adjusted_width = height_inches * aspect_ratio_global
        fig_global.set_size_inches(adjusted_width, height_inches)
    else:
        adjusted_height = width_inches / aspect_ratio_global
        fig_global.set_size_inches(width_inches, adjusted_height)

    new_font_size = font_size_global * fig_global.get_size_inches()[0] / 6.0
    new_line_width = line_width_global * fig_global.get_size_inches()[0] / 6.0

    fig_global.set_linewidth(new_line_width)
    for label in ax_global.get_xticklabels() + ax_global.get_yticklabels():
        label.set_fontsize(new_font_size)
    ax_global.xaxis.label.set_fontsize(new_font_size)
    ax_global.yaxis.label.set_fontsize(new_font_size)
    fig_global.canvas.draw()

# 注册全局事件处理函数
fig_global.canvas.mpl_connect('resize_event', on_resize_global)

# 隐藏工具栏
rcParams['toolbar'] = 'None'

