import numpy as np
import pandas as pd
results_A = []
# 准则层的成对比较矩阵
A = np.array([
    [1, 1/2, 4, 3, 3],
    [2, 1, 7, 5, 5],
    [1/4, 1/7, 1, 1/2, 1/3],
    [1/3, 1/5, 2, 1, 1],
    [1/3, 1/5, 3, 1, 1]
])

eigenvalues, eigenvectors = np.linalg.eig(A)
# 找到最大特征值的索引
max_eigenvalue_index = np.argmax(eigenvalues)
# 最大特征值和对应的特征向量
max_eigenvalue = eigenvalues[max_eigenvalue_index]
max_eigenvector = eigenvectors[:, max_eigenvalue_index]
normalized_weights = max_eigenvector / np.sum(max_eigenvector)
results_A.append((max_eigenvalue, normalized_weights))

# RI 值
RI = np.array([0, 0, 0.52, 0.89, 1.12, 1.26, 1.36, 1.41, 1.46, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59, 1.60, 1.61, 1.615, 1.62, 1.63])

# 计算 CI
CI = (max_eigenvalue - len(A)) / (len(A) - 1)

# 计算一致性比率 CR
CR = CI / RI[len(A)-1]  # 使用 RI 的最后一个值

print("CI:", CI)
print("CR:", CR)

# 定义成对比较矩阵列表
B_matrices = [
    np.array([
        [1, 2, 5],
        [1/2, 1, 2],
        [1/5, 1/2, 1]
    ]),
    np.array([
        [1, 1/3, 1/8],
        [3, 1, 1/3],
        [8, 3, 1]
    ]),
    np.array([
        [1, 1, 3],
        [1, 1, 3],
        [1/3, 1/3, 1]
    ]),
    np.array([
        [1, 3, 4],
        [1/3, 1, 1],
        [1/4, 1, 1]
    ]),
    np.array([
        [1, 1, 1/4],
        [1, 1, 1/4],
        [4, 4, 1]
    ])
]
# 存储每个矩阵的结果
results_B = []
CI_values = []  # 存储每组矩阵的 CI 值
CR_values = []  # 存储每组矩阵的 CR 值
# 计算特征值和权值向量，并存储结果
for idx, matrix in enumerate(B_matrices):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    max_eigenvalue_index = np.argmax(eigenvalues)
    max_eigenvalue = eigenvalues[max_eigenvalue_index]
    weights_vector = eigenvectors[:, max_eigenvalue_index]
    normalized_weights = weights_vector / np.sum(weights_vector)  
    CI = (max_eigenvalue - len(matrix)) / (len(matrix) - 1)
    CR = CI / RI[len(matrix)-1]  # 使用 RI 的最后一个值
    results_B.append((max_eigenvalue, normalized_weights))

    CI_values.append(CI)
    CR_values.append(CR)
#一致性检验

