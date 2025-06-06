import numpy as np
n = 4
A = np.round(10*(np.random.rand(n,n)))
I = np.eye(n,n)
Z = np.zeros((n,n))

Q = np.array_equal(A , A@I)
print(Q)