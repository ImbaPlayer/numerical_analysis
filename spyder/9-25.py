# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:15:20 2020

@author: Administrator
"""
import numpy as np 
def cal1(x, y0):
    maxiter = 10
    print("x = {}".format(x))
    print("init value y0 = {}".format(y0))
    result = []
    abs_error = []
    relative_error = []
    right_reuslt = 1/np.sqrt(x)
    for _ in range(maxiter):
        yn = y0*(1.5 - 0.5*x*y0**2)
        y0 = yn
        temp_error = abs(right_reuslt - yn)
        result.append(yn)
        abs_error.append(temp_error)
        relative_error.append(temp_error / right_reuslt)
    print("right result", right_reuslt)
    print("iteration result", yn)
    print("cycle result", result)
    print("abs error", abs_error)
    for data in abs_error:
        print(data)
    print("relative error", relative_error)
    for data in relative_error:
        print(data)

# use special init value 
def cal2(n):
    maxiter = 10
    right_reuslt = 1/np.sqrt(x)
    y3 = np.array([n])
    y3 = y3.astype(np.float32)
    x2 = np.float64(y3[0]*0.5)
    ii = y3.view(np.int32)
    ii[:] = 0x5f3759df - (ii >> 1)
    result = []
    abs_error = []
    relative_error = []
    y = np.float64(y3[0])
    for _ in range(maxiter):
        y = y*(1.5-x2*y*y)
        temp_error = abs(right_reuslt - y)
        result.append(y)
        abs_error.append(temp_error)
        relative_error.append(temp_error / right_reuslt)
    print("right result", right_reuslt)
    print("iteration result", y)
    print("cycle result", result)
    print("abs error", abs_error)
    print("relative error", relative_error)
    for data in abs_error:
        print(data)
    print("relative error", relative_error)
    for data in relative_error:
        print(data)
    return y
    

if __name__ == "__main__":
    x = np.float64(2)
    y0 = np.float64(0.5)
    cal1(x, y0)
    print()
    cal2(x)