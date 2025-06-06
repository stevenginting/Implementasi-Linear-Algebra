
import numpy as np

# Generate random arrays
a = 3*np.round(np.random.randn(3,3))
b = 3*np.round(np.random.randn(3,3))

# Element-wise multiplication
x = np.matmul(a.T, b)
y = np.matmul(b, a)
# -----------------------------#

#_____________________________#
m = 4
n = 4
A = 7*np.round(np.random.rand(m,n)) 
B = 7*np.round(np.random.rand(m,n)) 

C1 = np.zeros((m,m))
for i in range(n):
    C1 +=C1 + np.outer(A[:,i] ,B[i,:])

C2 = A@B

P = C1-C2
#---------------------------#
j = 2
L = np.random.randn(j,j)
I = np.random.randn(j,j)
V = np.random.randn(j,j)
E = np.random.randn(j,j)

# res1 = np.matrix.transpose(L@I@V@E)
# print(res1)
# res2 = E.T @ E.T @ V.T @ I.T
# print(res2), print('')
# print(res1 - res2)

#----------------#
M = np.array([[1,2,3],
              [4,5,6], 
              [7,8,9]])
V = np.array([1,2,3])
hasil = M@V
print(hasil)

