import scipy.linalg as li
import numpy as np
import itertools as it

# cal Inv of L matrix
def calLInv(L):
    # L = np.float64(np.random.randint(0,10,(3,3)))
    # L = np.tril(L)
    # print(L)
    L1 = np.float64(np.identity(L.shape[0]))
    # print(L1)
    for i in range(L.shape[0]):
        L1[i, i] = np.float64(1) / L[i, i]
        for j in range(i - 1, -1, -1):
            temp_sum = 0
            for k in range(j + 1, i + 1):
                temp_sum += L1[i, k] * L[k, j]
            L1[i, j] = (-np.float64(1) / L[j, j]) * temp_sum
    # print(L1)
    # print(np.linalg.inv(L))
    # print(np.dot(L, L1))
    # print(np.dot(L, np.linalg.inv(L)))
    return L1

# cal Inv of A by A-1 = U-1L-1
def calAInv(A):
    print("det", np.linalg.det(A))
    print(A)
    L, U = LU(A)
    L_inv = calLInv(L)
    U_inv = calLInv(U.T).T
    A_inv = np.dot(U_inv, L_inv)
    print("LL_inv", np.dot(L, L_inv))
    print("UU_inv", np.dot(U, U_inv))
    print("A_inv")
    print(A_inv)
    print(np.linalg.inv(A))
    print(np.dot(A, A_inv))
    print(np.dot(A, np.linalg.inv(A)))
    print(np.linalg.det(A) * np.linalg.det(A_inv))
    print(np.linalg.det(A) * np.linalg.det(np.linalg.inv(A)))