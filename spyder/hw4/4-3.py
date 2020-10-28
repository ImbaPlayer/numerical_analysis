import numpy as np
import scipy.linalg as li
import itertools as it
import math
import matplotlib.pyplot as plt

e = 1e-6
n_list = [20, 30, 50]
# n_list = [50]
def genMatrix(n):
    N = n * n
    A = np.zeros((N, N))
    A[np.arange(0, N), np.arange(0,N)] = 4
    
    A[np.arange(0, N-1), np.arange(1, N)] = -1
    A[np.arange(1, N), np.arange(0, N-1)] = -1
    for i in np.arange(n-1, N-1, n):
        A[i, i + 1] = 0
    for i in np.arange(n, N-1, n):
        A[i, i - 1] = 0
    
    A[np.arange(0, N-n), np.arange(n, N)] = -1
    A[np.arange(n, N), np.arange(0, N-n)] = -1
    return A

# 计算迭代次数
def getK(B, s):
    w, v = li.eig(B)
    w_max = np.max(np.abs(w))
    k = s * math.log(10) / - math.log(w_max)
    return k

def G(A, b, n):
    I = np.identity(n)
    L = np.zeros((n,n))
    for i in range(n):
        L[i, np.arange(0, i)] = - A[i, np.arange(0, i)]
    #print(D)
    D = np.zeros((n,n))
    for i in range(n):
        D[i, i] = A[i, i]
    B = I - np.dot(li.inv(D), A)
    # w, v = li.eig(B)
    # w_max = np.max(np.abs(w))
    # print("w_max", w_max)
    f = np.inner(li.inv(D), b)
    # x0 = np.zeros(n)
    x0 = np.ones(n)

    times = 0
    # print("cal times", getK(B, 6))
    while(True):
        x = np.inner(B, x0) + f
        times += 1
        # if np.linalg.norm(x, ord=np.inf) < e:
        #     break
        if np.max(np.abs(x - x0)) < e:
            break
        x0 = x
        
    # print("x", x)
    print("J actual times", times)
    return x
    

def SOR(A, b, n, w):
    I = np.identity(n)
    L = np.zeros((n, n))
    for i in range(n):
        L[i, np.arange(0, i)] = - A[i, np.arange(0, i)]
    D = np.zeros((n, n))
    D[np.arange(0, n), np.arange(0, n)] = A[np.arange(0, n), np.arange(0, n)]
    U = np.zeros((n, n))
    for i in range(n):
        U[i, np.arange(i + 1, n)] = - A[i, np.arange(i + 1, n)]
    # print(A)
    # print(L)
    # print(D)
    # print(U)
    tmep_A = li.inv(D - w*L)
    temp_B = w*U + (1-w)*D
    B = np.dot(tmep_A, temp_B)
    f = np.inner(w*tmep_A, b)

    x0 = np.ones(n)

    times = 0
    # print("cal times", getK(B, 6))
    while(True):
        x = np.inner(B, x0) + f
        times += 1
        # if np.linalg.norm(x, ord=np.inf) < e:
        #     break
        if np.max(np.abs(x - x0)) < e:
            break
        x0 = x
        
    # print("x", x)
    print("SOR actual times", times)
    
    return x, times

def getBestW(A, n):
    I = np.identity(n)
    L = np.zeros((n,n))
    for i in range(n):
        L[i, np.arange(0, i)] = - A[i, np.arange(0, i)]
    #print(D)
    D = np.zeros((n,n))
    for i in range(n):
        D[i, i] = A[i, i]
    B = I - np.dot(li.inv(D), A)

    w, v = li.eig(B)
    w_max = np.max(np.abs(w))
    # print("w_max", w_max)
    wb = 2 / (1 + math.sqrt(1 - w_max * w_max))
    print("best wb", wb)

def myPlot(x, y, k):
    
    plt.subplot(1,3,k)
    plt.plot(x, y)
    plt.xlabel("w", fontsize=15)
    plt.ylabel("iteration times", fontsize=15)
    plt.title("n = {}".format(n_list[k-1]), fontsize=20)
    # plt.ylim(10, 200)
    plt.xlim(1, 1.9)
    plt.xticks(np.linspace(1,1.9,10,endpoint=True))

def solve(n, k):
    A = genMatrix(n)
    N = n*n

    # B = np.zeros((n, n))
    # temp = int(n / 2)
    # B[temp, temp] = 1
    # b = np.ravel(B)

    B = np.zeros((n, n))
    temp = int(n / 2)
    B[temp, int(n*0.4)] = -1
    B[temp, int(n*0.6)] = -1
    b = np.ravel(B)

    getBestW(A, N)
    w_list = [1 + 0.1 * i for i in range(10)]
    SOR_times = []
    for w in w_list:
        print("w = ", w)
        temp_x, temp_time = SOR(A, b, N, w)
        SOR_times.append(temp_time)
        print()
    myPlot(w_list, SOR_times, k)

def main():
    plt.figure(figsize=(8,6), dpi=80)
    k = 1
    for n in n_list:
        solve(n, k)
        k += 1
    plt.show()

def testContourf(V):
    plt.figure(figsize=(10,10))
    plt.contourf(V, 50)
    plt.ylim(0, 50)
    plt.xlim(0, 50)
    plt.show()

def testOne():
    n = 50
    A = genMatrix(n)
    N = n*n
    B = np.zeros((n, n))
    temp = int(n / 2)
    B[temp, temp] = 1
    b = np.ravel(B)
    # x = G(A, b, N)
    x, temp_time = SOR(A, b, N, 1.8)
    X = x.reshape((n,n))
    print(x)
    print(X)
    testContourf(X)

def testTwo():
    n = 50
    A = genMatrix(n)
    N = n*n
    B = np.zeros((n, n))
    temp = int(n / 2)
    B[temp, int(n*0.4)] = -1
    B[temp, int(n*0.6)] = 1
    b = np.ravel(B)
    # print(B)
    # print(b)
    # x = G(A, b, N)
    x, temp_time = SOR(A, b, N, 1.8)
    X = x.reshape((n,n))
    print(x)
    print(X)
    testContourf(X)

if __name__ == "__main__":
    # testOne()
    testTwo()
    # main()