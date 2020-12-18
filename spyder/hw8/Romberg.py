# -*- coding: utf-8 -*-
# @Author: Guanglin Duan
# @Date:   2020-12-18 16:59:19
# @Last Modified by:   Guanglin Duan
# @Last Modified time: 2020-12-18 19:06:46

import scipy.linalg as li
import numpy as np
import itertools as it
import math
import matplotlib.pyplot as plt

def f_sin(x):
    return (10/x)**2 * np.sin(10/x)

def tixing(a, b, n, f):
    x = np.linspace(a, b, n+1, endpoint=True)
    # print(x)
    # print(x[1:-1])
    h = (b - a) / n
    result = 2*np.sum(f(x[1:-1])) + f(a) + f(b)
    return h / 2 * result

def solve(a, b, f):
    T = [[0]]
    h = b-a
    T[0][0] = h/2*(f(a) + f(b))
    h = (b-a) / 2**1
    T.append([0 for i in range(2)])
    T[1][0] = h/2*(f(a) + 2*f((a+b)/2) + f(b))
    T[1][1] = (4*T[1][0] - T[0][0]) / (4 - 1)
    error = np.abs(T[1][1] - T[0][0])
    j = 2
    while error > 1e-6:
        h = (b-1) / 2**j
        T.append([0 for i in range(j + 1)])
        T[j][0] = tixing(a, b, 2**j, f)
        for k in range(1, j+1):
            T[j][k] = (4**k*T[j][k-1] - T[j-1][k-1]) / (4**k - 1)
        error = np.abs(T[j][j] - T[j-1][j-1])
        j += 1
    print(len(T) - 1)
    for data in T:
        print(data)    
def main():
    a = 1
    b = 3
    solve(a, b, f_sin)

if __name__ == "__main__":
    main()
