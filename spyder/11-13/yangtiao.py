# -*- coding: utf-8 -*-
# @Author: Guanglin Duan
# @Date:   2020-11-28 11:46:43
# @Last Modified by:   Guanglin Duan
# @Last Modified time: 2020-11-28 13:57:02
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.linalg as li

x_list = np.array([0.9,1.3,1.9,2.1,2.6,3.0,3.9,4.4,4.7,
            5.0,6.0,7.0,8.0,9.2,10.5,11.3,11.6,12.0,
            12.6,13.0,13.3])
y_list = np.array([1.3,1.5,1.85,2.1,2.6,2.7,2.4,2.15,2.05,
            2.1,2.25,2.3,2.25,1.95,1.4,0.9,0.7,0.6,
            0.5,0.4,0.25])

def DivDiff(x, f, order):
    n = x.size
    val = []
    currDD = f.copy()
    l = n
    for i in range(1, order + 1):
        diffx = x[i:n] - x[0:n-i]
        df = currDD[1:l] - currDD[0:l-1]
        l = l-1
        currDD = np.zeros((l,))
        currDD = df/diffx
        val.append(currDD)
    return val

def get_M():
    n = x_list.size - 1
    # 得到二阶均差
    ave = DivDiff(x_list, y_list, 2)
    # d0 = 6*f[x0,x0,x1]
    d = [6*(y_list[1] - y_list[0]) / (x_list[1] - x_list[0])**2]
    for data in ave[1]:
        d.append(data*6)
    # dn = 6*f[xn-1,xn,xn]
    d.append(6*(y_list[n-1]-y_list[n])/(x_list[n]-x_list[n-1])**2)
    hj = [0 for i in range(n)]
    for i in range(0, n):
        hj[i] = x_list[i+1] - x_list[i]
    # u_j
    uj = [0 for i in range(n)]
    lj = [0 for i in range(n)]
    for i in range(1, n):
        temp_result = hj[i - 1]/(hj[i-1] + hj[i])
        uj[i] = temp_result
        lj[i] = 1-temp_result
    # AM
    A = np.zeros((n+1, n+1))
    A[0,1] = 1
    A[n,n-1] = 1
    for i in range(n+1):
        A[i,i] = 2
    for i in range(1, n):
        A[i, i-1] = uj[i]
        A[i, i+1] = lj[i]
    # M
    M = li.solve(A,d)
    return M, hj

def get_M_2(M0, Mn):
    n = x_list.size - 1
    # 得到二阶均差
    ave = DivDiff(x_list, y_list, 2)
    # d0 = 6*f[x0,x0,x1]
    d = [6*(y_list[1] - y_list[0]) / (x_list[1] - x_list[0])**2]
    for data in ave[1]:
        d.append(data*6)
    # dn = 6*f[xn-1,xn,xn]
    d.append(6*(y_list[n-1]-y_list[n])/(x_list[n]-x_list[n-1])**2)
    hj = [0 for i in range(n)]
    for i in range(0, n):
        hj[i] = x_list[i+1] - x_list[i]
    # u_j
    uj = [0 for i in range(n)]
    lj = [0 for i in range(n)]
    for i in range(1, n):
        temp_result = hj[i - 1]/(hj[i-1] + hj[i])
        uj[i] = temp_result
        lj[i] = 1-temp_result
    # AM
    A = np.zeros((n-1, n-1))
    for i in range(n-1):
        A[i,i] = 2
    for i in range(1, n-1):
        A[i, i-1] = uj[i+1]
    for i in range(n-2):
        A[i, i+1] = lj[i+1]
    # M 
    b = d[1:n]
    b[0] = b[0] - uj[1] * M0
    b[n-2] = b[n-2] - lj[n-1]*Mn
    print("shape")
    print(A.shape)
    print(len(b))
    M = li.solve(A,b)
    M = np.concatenate(([M0], M, [Mn]))
    # M.append(Mn)
    return M, hj

def find_x(x, x_list):
    for i in range(len(x_list)-1):
        if x > x_list[i] and x < x_list[i + 1]:
            return i

def solve(x, M, h):
    for i in range(len(x_list)):
        if x == np.array(x_list[i]):
            return y_list[i]
    j = find_x(x, x_list)
    result = M[j]/(6*h[j])*((x_list[j+1]-x)**3) + M[j+1]/(6*h[j])*((x - x_list[j])**3) + (y_list[j]-M[j]*(h[j]**2)/6)*(x_list[j+1]-x)/h[j] + (y_list[j+1]-M[j+1]*(h[j]**2)/6)*(x-x_list[j])/h[j]
    return result
        

if __name__ == "__main__":
    x_test = np.linspace(0.9,13.3,125)
    # M_1, h_1 = get_M()
    M_1, h_1 = get_M_2(0,0)
    M_2, h_2 = get_M_2(10,10)
    M_3, h_3 = get_M_2(100,100)
    y_test_1 = [solve(i, M_1, h_1) for i in x_test]
    y_test_2 = [solve(i, M_2, h_2) for i in x_test]
    y_test_3 = [solve(i, M_3, h_3) for i in x_test]
    
    plt.plot(x_test, y_test_1, c="g", label="0")
    plt.plot(x_test, y_test_3, c="b",label="10")
    plt.plot(x_test, y_test_2, c="y",label="100")
    plt.scatter(x_list, y_list,c="r")
    plt.title("II-boundary conditions", fontsize=20)
    plt.legend()
    plt.show()