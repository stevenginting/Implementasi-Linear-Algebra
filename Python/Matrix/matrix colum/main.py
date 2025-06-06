import numpy as np
import matplotlib.pyplot as plt

m = 5
n = 5

A =  np.random.randn(m,n)

A[:,0] = A[:1]

print(np.array(Matrix(A)))
 