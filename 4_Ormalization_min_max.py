# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 20:38:12 2023

@author: 海sir
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 读取数据文件
data = pd.read_csv("ending.csv")  # 请将文件路径替换为你的数据文件路径

# 获取维度数据列
dimension_columns = ["X1", "X2", "X3", "X4"]
#选择最大最小规约或者标准化规约取决于你接下来的建模过程
# 创建MinMaxScaler对象
scaler = MinMaxScaler()
#scaler = StandardScaler()

# 对每个维度数据进行Min-Max规约
data[dimension_columns] = scaler.fit_transform(data[dimension_columns])

# 保存归一化后的数据到新的CSV文件
normalized_data_file = "minmax_normalized_ending.csv"
data.to_csv(normalized_data_file, index=False)

print("Normalized data saved to", normalized_data_file)
