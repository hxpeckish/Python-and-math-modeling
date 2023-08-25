import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 假设 data 是你的 DataFrame，label 列包含了鸢尾花的类别
data = pd.read_csv("minmax_normalized_ending.csv")  # 请将文件路径替换为你的数据文件路径
data = data.iloc[:, 1:]

# 设置绘图风格为科研论文风格
sns.set_style("whitegrid")
sns.set_palette("Set2")

# 绘制散点图，hue 参数表示按照标签不同着色
plot = sns.pairplot(data, hue="label", diag_kind="kde", markers=["o", "s", "D"])

plot._legend.remove()

# 手动创建图例
handles = plot._legend_data.values()
labels = plot._legend_data.keys()
plt.legend(handles, labels, loc="upper right")

# 设置图表标题
plt.suptitle("Scatter Plot of Iris Flowers Features", y=1.02, fontsize=16)

# 调整子图之间的距离和布局
plt.tight_layout()

# 显示图表
plt.show()
