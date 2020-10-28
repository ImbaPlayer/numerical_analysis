import numpy as np
import matplotlib.pyplot as plt

def testContourf():
    plt.figure(figsize=(10,10))
    V = np.random.random((10, 10))
    print(V)
    plt.contourf(V, 50)
    plt.show()

def testSOR():
    n = 5
    B = np.zeros((n, n))
    temp = int(n / 2)
    B[temp, temp] = 1
    print(B)
    C = np.ravel(B)
    print(C)
    D = C.reshape((n, n))
    print(D)

if __name__ == "__main__":
    # a = 1e-6
    # print(a * 10)
    # A = np.ones((2,2))
    # B = 2*A
    # print(A)
    # print(B)
    # C = np.arange(2, 8, 3)
    # print(C)
    # testContourf()
    testSOR()