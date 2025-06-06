import numpy as np

# 1. Matriks acak 6x6
np.random.seed(42)  # biar hasil tetap sama setiap run
A = np.random.randint(1, 10, size=(6, 6))

print(A)

det1 = np.linalg.det(A)
print("Hasil determinan pertama adalah:",det1)

#Pertukaran baris pertama
A_swap1 = A.copy()
A_swap1[[3,5]] = A[[5,3]]
det2 = np.linalg.det(A_swap1)
print("Hasil dari determinan kedua adalah",det2)

#Pertukaran kedua
A_swap2 = A.copy()
A_swap2[[5,1]] = A_swap2[[1,5]]
print(A_swap2)