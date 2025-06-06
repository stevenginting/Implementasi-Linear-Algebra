import numpy as np

m = 5

A = np.round(np.random.randn(m,m))
C = A@A.T


V = np.random.randn(m)
W = np.random.rand(m)

Z = np.dot(A@V,W) - np.dot(V,A@W)
print(Z)

