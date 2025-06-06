import numpy as np
import matplotlib.pyplot as plt
import math 

m = 9
n = 4

A = 3.7*np.round(np.random.randn(m,n))
B = 3.7*np.round(np.random.randn(m,n))

Av = np.reshape(A,m*n,order='F')
Bv = np.reshape(B,m*n,order='F')
frob_dp = np.dot(Av,Bv)

frop_dp2 = np.trace(A.T@B)
print(frob_dp)
print(frop_dp2) ,print('')

Anorm = np.linalg.norm(A, 'fro')
Anorm2 = np.sqrt(np.trace(A.T@A))
print(Anorm), 
print(Anorm2)