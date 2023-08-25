import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline

# 假设 data 是你的 DataFrame，label 列包含了鸢尾花的类别
data = pd.read_csv("proceess2.csv")  # 请将文件路径替换为你的数据文件路径
missing_values = data.isnull()  # 返回一个与 data 大小相同的布尔型 DataFrame
rows_with_missing_values = data[data.isnull().any(axis=1)]
print(rows_with_missing_values)
print("\n")
# 按照 label 列进行分组
grouped = data.groupby("label")

# 定义要插值的列名列表
columns_to_interpolate = ["X1", "X2", "X3", "X4"]
for label, group_data in grouped:
    for col in columns_to_interpolate:
        current_data = group_data.copy()
        #获得缺失值的索引，根据索引设置缺失值
        missing_index = current_data[current_data[col].isnull()].index
        current_data.loc[missing_index, col] = np.nan
        # 使用线性插值填充缺失值
        current_data[col].interpolate(method="linear", inplace=True)
        # 获取列的数据
        x = current_data[col].values
        # 创建 CubicSpline 插值对象
        cs = CubicSpline(range(len(x)), x)
        # 插值得到新的数据
        new_x = cs(range(len(x)))
        # 将插值后的数据更新回原始 DataFrame
        current_data[col] = new_x  
        # 将处理后的数据更新回原始的 data 数据中
        data.update(current_data)      
# 假设 data 是你的处理后的 DataFrame
missing_values = data.isnull()  # 返回一个与 data 大小相同的布尔型 DataFrame
rows_with_missing_values = data[data.isnull().any(axis=1)]
print(rows_with_missing_values)
data.to_csv("ending.csv", index=False)
