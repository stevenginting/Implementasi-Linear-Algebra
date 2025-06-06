import numpy as np
import matplotlib.pyplot as plt
import math

v = np.array([3, -2])
teta = np.linspace(0, 2*np.pi, 100)
vekmags = np.zeros((len(teta), 2))

for i in range(len(teta)):
    th = teta[i]
    
    # Matriks Pure Rotation
    pr = np.array([[math.cos(th), -math.sin(th)], 
                   [math.sin(th), math.cos(th)]])
    
    # Matriks Impure Rotation (Rotasi + Scaling)
    ir = np.array([[2 * math.cos(th), -math.sin(th)], 
                   [-math.sin(th), math.cos(th)]])
    
    # Simpan hasil norm dari vektor yang telah dirotasi
    vekmags[i, 0] = np.linalg.norm(pr @ v.T)  # Pure rotation
    vekmags[i, 1] = np.linalg.norm(ir @ v.T)  # Impure rotation

# Plot hasil rotasi
plt.plot(teta, vekmags[:, 0], label='Pure Rotation', color='blue')
plt.plot(teta, vekmags[:, 1], label='Impure Rotation', color='red', linestyle='dashed')

plt.xlabel('Theta (radians)')
plt.ylabel('Magnitude of Transformed Vector')
plt.title('Comparison of Pure and Impure Rotation')
plt.legend()
plt.grid()
plt.show()
