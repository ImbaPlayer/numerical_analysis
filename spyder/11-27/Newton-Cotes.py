import scipy.linalg as li
import numpy as np
import itertools as it
import math
import matplotlib.pyplot as plt

C = np.array([[1/2, 1/2],
        [1/6, 4/6, 1/6],
        [1/8, 3/8, 3/8, 1/8],
        [7/90, 16/45, 2/15, 16/45, 7/90],
        [19/288, 25/96, 25/144, 25/144, 25/96, 19/288],
        [41/840, 9/35, 9/280, 34/105, 9/280, 9/35, 41/840],
        [751/17280, 3577/17280, 1323/17280, 2989/17280, 2989/17280,1323/17280,3577/17280,751/17280],
        [989/28350, 5888/28350, -928/28350, 10496/28350, -4540/28350, 10496/28350,-928/28350,5888/28350,989/28350]])

def f_log(x):
    return np.log(x)

def f_sin(x):
    return (10/x)**2 * np.sin(10/x)

def NC(a, b, n, f):
    x = np.linspace(a, b, n+1, endpoint=True)
    result = np.sum(C[n-1] * f(x))
    
    return (b-a) * result

if __name__ == "__main__":
    # getC()
    for i in range(1, 9):
        result = NC(1, 2, i, f_log)
        print(result)
    print()
    for i in range(1, 9):
        result = NC(1, 3, i, f_sin)
        print(result)