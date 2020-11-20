import scipy.linalg as li
import numpy as np
import itertools as it
import math
import matplotlib.pyplot as plt

cond_list = []
def get_A(n, x):
    A = np.zeros((n+1, n+1))
    for i in range(n+1):
        for j in range(n+1):
            A[i, j] = np.sum(np.power(x, i+j))
    cond_list.append(Cond(A, 2))
    return A

def get_b(n, x, y):
    b = np.zeros(n+1)
    for i in range(n+1):
        b[i] = np.sum(np.dot(y, np.power(x, i)))
    return b

def solve(n, x, y):
    A = get_A(n, x)
    # A += 0.1
    b = get_b(n, x, y)
    a = li.solve(A, b)
    return a

def fx(n, a, x):
    result = 0
    for i in range(n+1):
        result += a[i] * x**i
    return result

# ord = 1, 2, np.inf
def Cond(A, ord):
    A_inv = np.linalg.inv(A)
    A_norm = np.linalg.norm(A, ord=ord)
    A_inv_norm = np.linalg.norm(A_inv, ord=ord)
    cond = A_norm * A_inv_norm
    return cond

def main():
    x = [i * 0.1 for i in range(10)]
    y = [0.97, 0.83, 0.65, 0.54, 0.46, 0.36, 0.29, 0.25, 0.21, 0.17]
    plt.figure(figsize=(10,10))
    error_list = []
    # plt.subplot(1,2,1)
    plt.scatter(x, y)
    for n in range(1, 9):
        a = solve(n,x,y)
        x_test = np.linspace(0,1,50)
        y_test = fx(n,a, x_test)
        y_error = fx(n,a, np.array(x))
        error = li.norm(y_error-np.array(y), ord=2)
        error_list.append(error)
        plt.plot(x_test, y_test, label="n={},cond={:.2e}".format(n, cond_list[n-1]))
    # x_error = [i for i in range(1,10)]
    # plt.scatter(np.array(x_error), error_list)
    print("error", error_list)
    print("cond", cond_list)
    # plt.subplot(1,2,2)
    # plt.plot(x_error, error_list, label="error")
    # plt.plot(x_error, cond_list, label="cond")
    plt.legend()
    plt.show()    

if __name__ == "__main__":
    main()