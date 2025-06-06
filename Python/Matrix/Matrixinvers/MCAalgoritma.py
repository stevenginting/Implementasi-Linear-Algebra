import numpy as np

m = 4
A = np.random.randint(1, 10, size=(m, m))

minors = np.zeros((m, m))
H = np.zeros((m, m))

for i in range(m):
    for j in range(m):

        rows = [True]*m
        cols = [True]*m
        rows[i] = False
        cols[j] = False

        # Ambil submatrix dengan np.ix_
        submatrix = A[np.ix_(rows, cols)]

        minors[i, j] = np.linalg.det(submatrix)
        H[i, j] = (-1)**(i + j)

C = H * minors  # Cofactor matrix

Ainv = C.T / np.linalg.det(A)  # Adjoint / Determinant

print("Matrix A:")
print(A)

print("\nMatrix A inverse:")
print(Ainv)

print("\nA @ Ainv (harus mendekati identitas):")
print(np.round(A @ Ainv, 2))
