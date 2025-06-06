import numpy as np
import matplotlib.pyplot as plt
m = 3

A = np.random.randint(1,10,size=(m,m))

Ainv = np.linalg.inv(A)
print("Hasil dari invers adalah:",Ainv)

idm = A@Ainv
print("Hasil dari perkalian invers adalah",idm)

plt.subplot(131)
plt.imshow(A)
plt.title('Matrix A')

plt.subplot(132)
plt.imshow(Ainv)
plt.title('Matrix $A^{-1}$')

plt.subplot(133)
plt.imshow(idm)
plt.title('AA^{-1}$')

plt.show()