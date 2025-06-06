import numpy as np

A = np.random.randint(1,9,size=(2,2))
A = np.diag((np.arange(1,6)))

print(A) , print('')
print(np.linalg.inv(A))