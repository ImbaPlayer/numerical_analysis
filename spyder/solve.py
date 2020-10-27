# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:50:01 2020

@author: Administrator
"""

import scipy.linalg as li
import numpy as np
import itertools as it

def mySolve(A, b):
    print("mySolve float64")
    Ab = np.c_[A,b]
    # print(Ab)
    for i in range(n):
        a = Ab[i,i]
        for j in range(i + 1, n):
            l = Ab[j,i] / a
            Ab[j] += -l * Ab[i]
        # print(Ab)
    d = Ab[:,n]
    x = np.zeros(n)
    x[n-1] = d[n-1] / Ab[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = (d[i] - np.inner(Ab[i, i+1:n], x[i + 1:n])) / Ab[i,i]
    print(x)

def mySolve16(A, b):
    print("mySolve float16")
    Ab = np.c_[A,b]
    Ab = np.float16(Ab)
    # print(Ab)
    for i in range(n):
        a = Ab[i,i]
        for j in range(i + 1, n):
            l = Ab[j,i] / a
            Ab[j] += -l * Ab[i]
        # print(Ab)
    d = Ab[:,n]
    x = np.zeros(n)
    x[n-1] = d[n-1] / Ab[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = (d[i] - np.inner(Ab[i, i+1:n], x[i + 1:n])) / Ab[i,i]
    print(x)
def test():
    n = 2
    A = np.float64(np.random.randn(n,n))
    B = np.float16(A)
    print(A)
    print(B)
if __name__ == "__main__":
    n = 5
    A = np.float64(np.random.randint(0,10,(n,n)))
    detTure = np.float64(li.det(A))
    xTure = np.random.randn(n)
    b = np.inner(A,xTure)

    A[0, 0] = 0.001
    print("A = ")
    print(A)
    print("b = ")
    print(b)
    solv1 = li.solve(A,b)
    print("scipy solve")
    print(solv1)
    mySolve(A,b)
    mySolve16(A,b)
