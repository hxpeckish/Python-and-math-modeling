import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 从CSV文件中读取数据，将第一列作为索引
data = pd.read_csv("minmax_normalized_ending.csv", index_col=0)

# 获取标签列和特征列
labels = data['label']
features = data.drop('label', axis=1)  # 假设标签列名为'label'

# 设置Seaborn风格
sns.set(style="white")

# 添加颜色映射
color_palette = {'Iris-setosa': 'blue', 'Iris-versicolor': 'orange', 'Iris-virginica': 'green'}
colors = [color_palette[label] for label in labels]

# 绘制多变量散点图矩阵
sns.pairplot(features, diag_kind='kde', plot_kws={'alpha': 0.7, 's': 50, 'edgecolor': 'k', 'palette': colors})
plt.show()
