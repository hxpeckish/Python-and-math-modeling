import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 导入 Seaborn

# 设置 Seaborn 风格
sns.set(style="whitegrid")  # 使用白色网格风格

# 假设 data 是你的 DataFrame，label 列包含了鸢尾花的类别
data = pd.read_csv("process1_data.csv")  # 请将文件路径替换为你的数据文件路径

# 获取所有可能的标签
unique_labels = data["label"].unique()

# 定义要处理的列名列表
columns_to_process = ["X1", "X2", "X3", "X4"]

# 设置画布大小
plt.figure(figsize=(12, 8))  # 调整画布大小

# 定义颜色列表，每个类别使用不同的颜色
colors = sns.color_palette("Set2", n_colors=len(unique_labels))  # 使用 Seaborn 颜色方案

plot_number = 1

# 存储异常值的信息
outliers_info = []

for label, color in zip(unique_labels, colors):
    # 获取当前类别的数据
    subset_data = data[data["label"] == label]
    
    for col in columns_to_process:
        plt.subplot(len(unique_labels), len(columns_to_process), plot_number)
        
        # 绘制竖向箱线图，并设置颜色、标记和线型
        box = plt.boxplot(subset_data[col], vert=True, widths=0.5, notch=True, patch_artist=True, boxprops=dict(facecolor=color))
        plt.title(f"{label} - {col}")
        
        # 根据箱线图数据检测异常值，并将异常值替换为 NaN
        q1 = subset_data[col].quantile(0.25)
        q3 = subset_data[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        for i, value in enumerate(subset_data[col]):
            if value < lower_bound or value > upper_bound:
                outliers_info.append({"Label": label, "Row": subset_data.index[i], "Column": col, "Value": value})
                subset_data.at[subset_data.index[i], col] = None  # 替换为 NaN

        plot_number += 1
        
    # 将异常值更新到原始数据
    data.loc[subset_data.index, columns_to_process] = subset_data[columns_to_process]

# 打印异常值信息
for outlier in outliers_info:
    print("Label:", outlier["Label"], "- Row:", outlier["Row"], "- Column:", outlier["Column"], "- Value:", outlier["Value"])

# 设置图表标题和布局
plt.suptitle("Box Plots of Different Label Groups", y=1.02, fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# 继续进行后续处理，如数据插值等
data.to_csv("proceess2.csv", index=False)
