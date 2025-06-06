import numpy as np
import matplotlib.pyplot as plt

# Dimensi matriks
m, n = 6, 3

# Membuat matriks A
A = np.random.randn(m, n)

# Menghitung pseudo-invers
A_pinv = np.linalg.pinv(A)

# Verifikasi: A_pinv @ A mendekati identitas
I_approx = A_pinv @ A

# Menampilkan hasil
print("A_pinv @ A:")
print(I_approx)

# Visualisasi matriks
plt.subplot(131)
plt.imshow(A, cmap='viridis')
plt.title('Matriks A')
plt.axis('off')

plt.subplot(132)
plt.imshow(A_pinv, cmap='viridis')
plt.title('Pseudo-Invers A')
plt.axis('off')

plt.subplot(133)
plt.imshow(I_approx, cmap='viridis')
plt.title('A_pinv @ A')
plt.axis('off')

plt.tight_layout()
plt.show()
