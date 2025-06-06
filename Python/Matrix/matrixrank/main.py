import matplotlib.pyplot as plt
import numpy as np

m = 10
n = 10
r = 7
s =4

F = np.zeros((m,n))
B = np.zeros((m,n))

#reduced rank
u = np.random.randint(0,15,(m,r))
v = np.random.randint(0,15,(r,n))
R = u @ v
#skalar multiplication
l1 = s*F
l2 = s*R

print("Rank F (Full Zeros):", np.linalg.matrix_rank(F))
print("Rank R (Reduced Rank):", np.linalg.matrix_rank(R))
print("Rank l1 (Scalar x Full Zeros):", np.linalg.matrix_rank(l1))
print("Rank l2 (Scalar x Reduced Rank):", np.linalg.matrix_rank(l2))


if np.linalg.matrix_rank(l1) == s*np.linalg.matrix_rank(F):
        print(True)
else:
    print(False)