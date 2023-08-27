import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 设置 seaborn 风格
sns.set(style="whitegrid")

# 从 Excel 文件中读取数据
data_path = '熵权法.xlsx'
df = pd.read_excel(data_path)

# 提取数据和指标名称
data = df.values
indicators = df.columns

# 归一化处理
min_values = np.min(data, axis=0)
max_values = np.max(data, axis=0)
normalized_data = (data - min_values) / (max_values - min_values)

# 计算信息熵
def calculate_entropy(column):
    p = column / np.sum(column)
    return -np.sum(p * np.log(p + 1e-10)) / np.log(len(column))  # 加上一个小的值以避免对数为零

entropies = np.apply_along_axis(calculate_entropy, axis=0, arr=normalized_data)

# 计算权重
weights = (1 - entropies) / np.sum(1 - entropies)
final_weights = weights / np.sum(weights)  # 计算最终的百分比权重

# 绘制饼状图
plt.figure(figsize=(10, 6))
colors = sns.color_palette("pastel")
plt.pie(final_weights, labels=indicators, autopct='%.1f%%', colors=colors, startangle=140, wedgeprops={"edgecolor": "k", "linewidth": 1})
plt.title('各指标权重的饼状图')
plt.legend(loc='upper right', labels=[f'{indicator}: {weight*100:.2f}%' for indicator, weight in zip(indicators, final_weights)])
plt.show()

print("各指标的权重：")
for i, indicator in enumerate(indicators):
    print(f"{indicator}: {final_weights[i]*100:.3f}%")
