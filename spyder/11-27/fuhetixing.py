import scipy.linalg as li
import numpy as np
import itertools as it
import math
import matplotlib.pyplot as plt

def f_sin(x):
    return (10/x)**2 * np.sin(10/x)

def solve(a, b, n, f):
    x = np.linspace(a, b, n+1, endpoint=True)
    # print(x)
    # print(x[1:-1])
    h = (b - a) / n
    result = 2*np.sum(f(x[1:-1])) + f(a) + f(b)
    return h / 2 * result

def simpson(a, b, n, f):
    x = np.linspace(a, b, 2*n+1, endpoint=True)
    h = (b - a) / n
    result = 0
    for i in range(2, 2*n-1, 2):
        result += 2*f(x[i])
    for i in range(1, 2*n, 2):
        result += 4*f(x[i])
    result = h/6*(f(a) + result + f(b))
    return result

if __name__ == "__main__":
    sin_ans = -1.4260
    # for n in range(1, 1000):
    #     result = solve(1, 3, n, f_sin)
    #     if np.abs(sin_ans - result) < 1e-4:
    #         print("n", n)
    #         print(result)
    #         break
    for n in range(1, 1000):
        result = simpson(1, 3, n, f_sin)
        if np.abs(sin_ans - result) < 1e-5:
            print("n", n)
            print(result)
            break