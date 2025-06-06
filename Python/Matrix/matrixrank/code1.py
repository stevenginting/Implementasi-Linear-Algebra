import numpy as np

m = 10
n = 10
o = 4

A = np.random.randint(0,15,(m,o))
B = A @ np.random.randint(0,15,(o,6))
C = np.hstack((A,B))
print(np.linalg.matrix_rank(C))
print(np.shape(A))

x = 8
y = 47
z = 3

L = np.random.randint(0,15,(x,z)) @ np.random.randint(0,15,(z,y))
print(np.shape(L))
print(np.linalg.matrix_rank(L))
