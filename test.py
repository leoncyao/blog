import numpy as np

A = np.array([[1, 2], [1, 1]])

print(A)
b = np.array([6, 4])

print(np.linalg.solve(A, b))