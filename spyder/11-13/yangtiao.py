import numpy as np
import matplotlib.pyplot as plt
import math

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

def solve():
    n = x_list.size - 1
    print("n", n)
    print("len x_list", len(x_list))
    # 得到二階均差
    ave = DivDiff(x_list, y_list, 2)[1]
    ave = 6*ave
    d = [(y_list[1] - y_list[0] / x_list[1] - x_list[0])]
    for data in ave:
        d.append(data)
    print(ave)
    print("ave", len(ave))
    # h_j
    hj = [0 for i in range(n)]
    for i in range(1, n):
        hj[i] = x_list[i+1] - x_list[i]
    print(hj)
    print("hj", len(hj))
    # u_j
    uj = [0 for i in range(n)]
    lj = [0 for i in range(n)]
    for i in range(1, n):
        temp_result = hj[i - 1]/(hj[i-1] + hj[i])
        uj[i] = temp_result
        lj[i] = 1-temp_result
    print(len(uj))
    print(len(lj))
    # AM
    A = np.zeros((n+1, n+1))
    for i in range(n):
        A[i,i] = 2
    # print(A)
    for i in range(1, n):
        A[i, i-1] = uj[i]
        A[i, i+1] = lj[i]
    print(A)

    
        

if __name__ == "__main__":
    solve()