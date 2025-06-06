import numpy as np
import math
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi,100)
print(x)
xy = np.vstack((np.cos(x) , np.sin(x))).T

plt.plot(xy[:,1] , xy[:,1], 'o' )
plt.show()

# T = np.array([[1,2] , [2,1]])

# newxy = xy@T

# plt.plot(newxy[:,0] , newxy[:,1] ,'o')
# plt.axis('square')
# plt.show()