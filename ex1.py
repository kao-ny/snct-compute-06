import numpy as np

X = [
    [165, 53],
    [160, 47],
    [166, 55],
    [164, 56],
    [168, 55]
]

# 共分散
avg_height, avg_weight = np.average(X, axis=0)

tmp = 0
for x in X:
    diff_height = x[0] - avg_height
    diff_weight = x[1] - avg_weight
    tmp += diff_weight * diff_height

cov = (1/len(X)) * tmp
print('■ 共分散')
print(cov)

# 相関係数
var = [0, 0]
for x in X:
    var[0] += (x[0] - avg_height) ** 2
    var[1] += (x[1] - avg_weight) ** 2

var_height = (1/len(X)) * var[0]
var_weight = (1/len(X)) * var[1]

rho = cov / np.sqrt(var_height * var_weight)
print('■ 相関係数')
print(rho)
