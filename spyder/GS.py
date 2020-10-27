# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:58:12 2020

@author: Administrator
"""

import scipy.linalg as li
import numpy as np
import itertools as it
import math

def G(A, b, xTure):
    print(A)
    I = np.identity(n)
    L = np.zeros((n,n))
    for i in range(n):
        L[i, np.arange(0, i)] = - A[i, np.arange(0, i)]
    #print(D)
    D = np.zeros((n,n))
    for i in range(n):
        D[i, i] = A[i, i]
    print(D)
    B = I - np.dot(li.inv(D), A)
    print(B)
    w, v = li.eig(B)
    w_max = np.max(np.abs(w))
    print("w_max", w_max)
    f = np.inner(li.inv(D), b)
    x0 = np.zeros(n)
        
    # for i in range(500):
    #     x = np.inner(B, x0) + f
    #     x0 = x
    q = li.norm(B, ord=2)
    times = 0
    while(True):
        x = np.inner(B, x0) + f
        
        if np.max(np.abs(x - x0)) < 0.001:
            break
        x0 = x
        times += 1
    print("x", x)
    print("times", times)
    print("cal times", getK(B, 3))


def GS(A, b):
    I = np.identity(n)
    L = np.zeros((n,n))
    for i in range(n):
        L[i, np.arange(0, i)] = - A[i, np.arange(0, i)]
    #print(D)
    D = np.zeros((n,n))
    for i in range(n):
        D[i, i] = A[i, i]
    print(D)
    B = I - np.dot(li.inv(D - L), A)
    f = np.inner(li.inv(D - L), b)
    
    x0 = np.zeros(n)
        
    # for i in range(500):
    #     x = np.inner(B, x0) + f
    #     x0 = x
    w, v = li.eig(B)
    w_max = np.max(np.abs(w))
    print("w_max", w_max)
    times = 0
    while(True):
        x = np.inner(B, x0) + f
        
        if np.max(np.abs(x - x0)) < 0.001:
            break
        x0 = x
        times += 1
    print("x", x)
    print("times", times)
    print("cal times", getK(B, 3))

def getK(B, s):
    w, v = li.eig(B)
    w_max = np.max(np.abs(w))
    k = s * math.log(10) / - math.log(w_max)
    return k

if __name__ == "__main__":
    n = 5
    A = np.float64(np.random.randint(0,10,(n,n)))
    idx0 = np.arange(0, n)
    A[idx0, idx0] += 20
    detTure = np.float64(li.det(A))
    xTure = np.random.randn(n)
    b = np.inner(A,xTure)
    
    G(A, b, xTure)
    GS(A,b)
    print("xTrue", xTure)
