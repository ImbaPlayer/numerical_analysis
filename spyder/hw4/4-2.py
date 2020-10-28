import numpy as np
import scipy.linalg as li
import itertools as it
import math
import matplotlib.pyplot as plt


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
    while(True):
        x = np.inner(B, x0) + f
        times += 1
        if np.linalg.norm(x, ord=np.inf) < 1e-6:
            break
        x0 = x
        
    # print("x", x)
    print("J actual times", times)
    # print("cal times", getK(B, 6))

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
    while(True):
        x = np.inner(B, x0) + f
        times += 1
        if np.linalg.norm(x, ord=np.inf) < 1e-6:
            break
        x0 = x
        
    # print("x", x)
    print("SOR actual times", times)
    # print("cal times", getK(B, 6))
    return times

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
    print("w_max", w_max)
    wb = 2 / (1 + math.sqrt(1 - w_max * w_max))
    print("best wb", wb)


# 生成五对角矩阵
def matrix(n):
    A = np.zeros((n,n))
    A[np.arange(0, n), np.arange(0,n)] = 20
    A[np.arange(0, n-1), np.arange(1, n)] = -8
    A[np.arange(1, n), np.arange(0, n-1)] = -8
    A[np.arange(0, n-2), np.arange(2, n)] = 1
    A[np.arange(2, n), np.arange(0, n-2)] = 1
    return A

def myPlot(x, y, k):
    
    plt.subplot(1,3,k)
    plt.plot(x, y)
    plt.xlabel("w", fontsize=15)
    plt.ylabel("iteration times", fontsize=15)
    plt.title("n = {}".format(n_list[k-1]), fontsize=20)
    plt.ylim(10, 140)
    plt.xlim(1, 1.9)
    plt.xticks(np.linspace(1,1.9,10,endpoint=True))
    

def solve(n, k):
    A = matrix(n)
    b = np.zeros(n)
    G(A, b, n)
    getBestW(A, n)
    w_list = [1, 1.2, 1.25, 1.314, 1.4, 1.6, 1.8]
    w_list = np.arange(1, 2, 0.1)
    w_list = [1 + 0.1 * i for i in range(10)]
    SOR_times = []
    for w in w_list:
        print("w = ", w)
        SOR_times.append(SOR(A, b, n, w))
        print()
    myPlot(w_list, SOR_times, k)

if __name__ == "__main__":
    plt.figure(figsize=(8,6), dpi=80)
    k = 1
    n_list = [10, 20, 40]
    for n in n_list:
        solve(n, k)
        k += 1
    plt.show()