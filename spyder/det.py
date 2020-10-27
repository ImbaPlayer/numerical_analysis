# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:58:31 2020

@author: Administrator
"""

import scipy.linalg as li
import numpy as np
import itertools as it
import time
# 索引主对角元素
def indexA(A, i):
    idx0 = np.arange(0, n)
    idx1 = np.arange(i, n+i)
    idx1[idx1 > n-1] = idx1[idx1 > n-1]-n
    a = A[idx0, idx1]
    return a
    #np.product()
# 索引附对角元素
def indexB(A, i):
    idx0 = np.arange(0, n)
    idx1 = np.arange(i, i-n, -1)
    idx1[idx1 < 0] = idx1[idx1 < 0] + n
    print(idx1)
    a = A[idx0, idx1]
    return a
def calDet(A, n):
    result = 0
    for i in range(n):
        a = indexA(A, i)
        b = indexB(A, i)
        a1=np.prod(a)
        b1=np.prod(b)
        result += a1 - b1
    print(result)
    detTrue = np.float64(li.det(A))
    print(detTrue)
#求逆序数的函数
def inv_num(perSeq,n):
    ans = 0
    for i in range(n):
        for j in range(i):
            if perSeq[j]>perSeq[i]:
                ans +=1
    return ans
#使用遍历和逆序数求解
def calDetInv(A, n):
    result = 0
    for p in it.permutations(range(n)):
        idx1 = np.arange(0, n)
        idx2 = np.array(list(p))
        result += (-1)**inv_num(p, n) * np.prod(A[idx1, idx2])
    print(result)
    detTrue = np.float64(li.det(A))
    print(detTrue)
if __name__ == "__main__":
    n = 9
    A = np.random.randn(n, n) * 10
    start = time.time()
    calDetInv(A, n)
    end = time.time()
    print("time", end-start)