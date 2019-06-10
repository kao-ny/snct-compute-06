import numpy as np

X = [
    [86, 56, 92],
    [84, 52, 92],
    [90, 60, 95],
    [90, 60, 95],
    [87, 56, 87]
]

avg = np.average(X, axis=0)
M = []
for tmp in X:
    M.append(avg)

X = np.array(X)
M = np.array(M)

cov = (1/len(X)) * np.dot((X-M).T, (X-M))
print('■ 共分散行列')
print(cov)
