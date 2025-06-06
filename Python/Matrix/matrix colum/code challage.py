import numpy as np
import matplotlib.pyplot as plt

# Generate a square random matrix (20x20)
n = 20
matrix = np.random.rand(n, n)

# Impose a linear dependence (make one row a linear combination of others)
# This will make the matrix singular (determinant = 0) before shifting
matrix[0] = 0.5 * matrix[1] + 0.3 * matrix[2]  # Row 0 becomes a combination of rows 1 and 2

# Define lambda values from 0 to 1
lambda_values = np.linspace(0, 1, 1000)
determinants = []

# Repeat 1000 times for different lambda values
for lambda_val in lambda_values:
    # "Shift" the matrix (add lambda * identity matrix)
    shifted_matrix = matrix + lambda_val * np.eye(n)
    
    # Compute the absolute value of the determinant of the shifted matrix
    det = np.abs(np.linalg.det(shifted_matrix))
    determinants.append(det)

# Plot of determinant as a function of lambda
plt.figure(figsize=(10, 6))
plt.plot(lambda_values, determinants)
plt.xlabel('Lambda (λ)')
plt.ylabel('|Determinant|')
plt.title('Absolute Determinant as a Function of Lambda')
plt.grid(True)
plt.show()