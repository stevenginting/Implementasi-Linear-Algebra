import numpy as np
m = 2
n = 5
#fungsi

def rank_inequality(A, B):
    rank_A = np.linalg.matrix_rank(A)
    rank_B = np.linalg.matrix_rank(B)
    rank_A_plus_B = np.linalg.matrix_rank(A + B)
    
    return rank_A_plus_B <= min([rank_A, rank_B])

A = np.random.randint(0,10,(m,n))
B = np.random.randint(0,10,(m,n))

# TRANSPOSE
At = A.T
Bt = B.T

# RANKS
rA = np.linalg.matrix_rank(A)
rB = np.linalg.matrix_rank(B)

rAT = np.linalg.matrix_rank(At)
rBT = np.linalg.matrix_rank(Bt)

Rules = rank_inequality(A, B)

# OUTPUT
print(np.shape(Rules))
print(f"Hasil dari rules adalah: {Rules}")
print(f"Hasil dari rank A adalah: {rA} ")
print(f"Hasil dari rank B adalah: {rB} ")
print(f"Hasil dari rank A Transpose adalah: {rAT} ")
print(f"Hasil dari rank B Transpose adalah: {rBT} ") 


