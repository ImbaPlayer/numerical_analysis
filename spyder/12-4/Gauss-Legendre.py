# -*- coding: utf-8 -*-
# @Author: Guanglin Duan
# @Date:   2020-12-04 09:57:24
# @Last Modified by:   Guanglin Duan
# @Last Modified time: 2020-12-04 10:27:12

import scipy.linalg as li
import numpy as np
import itertools as it
import math
import matplotlib.pyplot as plt

def t2x(t, a, b):
    return (a+b)/2 + (b-a)/2*t


def f_sin(x):
    return (10/x)**2 * np.sin(10/x)

def my_solve(a, b, t, A):
    t = np.array(t)
    A = np.array(A)
    x = t2x(t, a, b)
    y = f_sin(x)
    result = np.sum(A * y)
    return result / 2 * (b-a)

def main():
    a = 1
    b = 3
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
        result = my_solve(a, b, t[i], A[i])
        print(result)

if __name__ == "__main__":
    main()
