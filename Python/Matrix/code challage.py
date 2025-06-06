import numpy as np
import matplotlib.pyplot as plt
import math 
m  = 3
A =  np.random.randn(m,m)
AtA = A.T@A

B = np.random.randn(m,m)
BtB = B.T@B

Cs = AtA -BtB

#-----------------------------------------------------------------------#
n = 4

A = 6*np.round(np.random.rand(n,n))
B = 3*np.round(np.random.rand(n,n))
C = np.diag(3*np.round(np.random.rand(n,n)))

#FULL

S = A@A
H = A*A


#DIAGONAL
s = C@C
h = C*C


#-------------------------------------------------#
def dft_method(n):
    omega = np.exp(-2j*np.pi/n)
    j,k = np.meshgrid(np.arange(n) , np.arange(n))
    F = omega **(j*k)
    return F

n = 4
F = dft_method(n)

#-----------------------------------------------------#
def MIA(A):
    Aanti = (A-A.T)/2
    mai = np.linalg.norm(Aanti) / np.linalg.norm(A)
    return mai

A = np.random.randn(5,5)
A = (A+A.T)/2

MIA(A)
p = 0
B = (1-p)*(A+A.T)/2 + p*(A-A.T)
print(B)