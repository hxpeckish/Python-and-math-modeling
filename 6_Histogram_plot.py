import pandas as pd
import matplotlib.pyplot as plt

# 从CSV文件中读取数据，将第一列作为索引
data = pd.read_csv("minmax_normalized_ending.csv", index_col=0)

# 获取标签和特征列
labels = data['label']
features = data.drop('label', axis=1)  # 假设标签列名为'label'

# 特征数量和标签数量
num_features = len(features.columns)
num_labels = len(labels.unique())

# 设置直方图布局
fig, axs = plt.subplots(num_features, 1, figsize=(8, 6))

# 针对每个特征绘制直方图
for feature_index, feature_name in enumerate(features.columns):
    for label in labels.unique():
        axs[feature_index].hist(features[labels == label][feature_name], bins=10, alpha=0.5, label=label)
    axs[feature_index].set_title(f'Feature "{feature_name}" Distribution')
    axs[feature_index].legend()

# 设置布局
plt.tight_layout()
plt.show()
