# -*- coding: utf-8 -*-
# @Author: Guanglin Duan
# @Date:   2020-12-04 10:29:44
# @Last Modified by:   Guanglin Duan
# @Last Modified time: 2020-12-04 11:00:05

import scipy.linalg as li
import numpy as np
import itertools as it
import math
import matplotlib.pyplot as plt

def t2x(t, a, b):
    return (a+b)/2 + (b-a)/2*t


def f_sin(x):
    return (10/x)**2 * np.sin(10/x)

def GL(x0, x1, t, A):
    t = np.array(t)
    A = np.array(A)
    x = t2x(t, x0, x1)
    y = f_sin(x)
    result = np.sum(A * y)
    return result / 2 * (x1-x0)


def solve(a, b, n, t, A):
    result = 0
    for k in range(n):
        x0 = a + k * (b-a)/n
        x1 = a + (k + 1) * (b-a)/n
        result += GL(x0, x1, t, A)
    return result

def main():
    t = np.array([
        [-np.sqrt(3)/3, np.sqrt(3)/3],
        [-0.7745967, 0, 0.7745967],
        [0.8611363, -0.8611363, 0.3399810, -0.3399810]
    ])
    A = np.array([
        [1, 1],
        [0.5555556, 0.8888889, 0.5555556],
        [0.3478548, 0.3478548, 0.6521452, 0.6521452]
    ])
    for i in range(3):
        print("阶数：{}".format(i + 2))
        for n in range(1, 50):
            result = solve(1, 3, n, t[i], A[i])
            print("n = {}, result = {}".format(n, result))
            if np.abs(result - (-1.426024756)) < 1e-6:
                break

if __name__ == "__main__":
    main()
