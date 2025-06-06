import numpy as np
import matplotlib.pyplot as plt

# Array untuk menyimpan hasil det(A) * det(B) dan det(AB)
dets = np.zeros((40, 2))

# Loop untuk matriks dari ukuran 1x1 hingga 40x40
for i in range(1, 41):  # mulai dari 1 hingga 40
    A = np.random.randint(1, i+1, size=(i, i))  # Matriks A dengan ukuran i x i
    B = np.random.randint(1, i+1, size=(i, i))  # Matriks B dengan ukuran i x i
    AB = A @ B  # Perkalian matriks A dan B

    # Menyimpan determinan dari A, B, dan AB
    dets[i-1, 0] = np.linalg.det(A) * np.linalg.det(B)  # det(A) * det(B)
    dets[i-1, 1] = np.linalg.det(AB)  # det(AB)

# Plot perbedaan antara det(A) * det(B) dan det(AB)
plt.plot(dets[:, 0] - dets[:, 1], 's')
plt.xlabel('Ukuran Matriks (n)')
plt.ylabel('Perbedaan Determinan (det(A) * det(B) - det(AB))')
plt.title('Perbedaan antara det(A) * det(B) dan det(AB) untuk Matriks Ukuran n')
plt.grid(True)
plt.show()
