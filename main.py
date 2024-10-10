import numpy as np

# Coefficient matrix A
A = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2],
    [3**10, 3**9, 3**8, 3**7, 3**6, 3**5, 3**4, 3**3, 3**2, 3],
    [4**10, 4**9, 4**8, 4**7, 4**6, 4**5, 4**4, 4**3, 4**2, 4],
    [5**10, 5**9, 5**8, 5**7, 5**6, 5**5, 5**4, 3**3, 3**2, 3]
])

# Right-hand side vector b
b = np.array([50, 200, 600, 1000, 2000, 3500, 5000, 10000, 20000, 50000])

# Solve the system using NumPy's linear algebra solver
x = np.linalg.solve(A, b)

print(x)