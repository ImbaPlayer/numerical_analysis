import numpy as np

def matrix(n):
    A = np.zeros((n,n))
    A[np.arange(0, n), np.arange(0,n)] = 20
    A[np.arange(0, n-1), np.arange(1, n)] = -8
    A[np.arange(1, n), np.arange(0, n-1)] = -8
    A[np.arange(0, n-2), np.arange(2, n)] = 1
    A[np.arange(2, n), np.arange(0, n-2)] = 1
    print(A)

if __name__ == "__main__":
    matrix(8)