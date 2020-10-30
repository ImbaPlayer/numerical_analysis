import numpy as np
import matplotlib.pyplot as plt
import math

eps = 1e-6
maxIter = 50
def g(x, b):
    return 2*x - b*x*x

def solve(b, x_0):
    itNum = 0
    err = 1
    result = [x_0]
    while err > eps and itNum <= maxIter:
        x_k = g(x_0, b)
        err = np.abs(x_k - x_0)
        x_0 = x_k
        itNum += 1
        print(itNum, x_k)
        result.append(x_k)
        if abs(x_k) > 1e5:
            print("error", x_k)
            return np.inf
    print("itNum", itNum)
    print("err", err)
    print("1/({})".format(b), result)
    print("right ans", 1 / b)
    return itNum

def new_g(x, b, l):
    return (1 + l) * x - b*l*x*x

def new_solve(b, l, x_0):
    itNum = 0
    err = 1
    result = [x_0]
    while err > eps and itNum <= maxIter:
        x_k = new_g(x_0, b, l)
        err = np.abs(x_k - x_0)
        x_0 = x_k
        itNum += 1
        print(itNum)
        result.append(x_k)
        if abs(x_k) > 1e5:
            print("error", x_k)
            return np.inf
    print("itNum", itNum)
    print("err", err)
    print("1/({})".format(b), result)
    print("right ans", 1 / b)
    return itNum

def myPlot(x_list, y_list, k):
    # x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    x = x_list
    y = y_list
    plt.subplot(1, 2, k)
    plt.plot(x, y)
    

if __name__ == "__main__":
    plt.figure(figsize=(8,4))
    it_list = []
    x_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    for data in x_list:
        print("x_0", data)
        it_list.append(solve(3, data))
    print(it_list)
    myPlot(x_list, it_list, 1)

    it_list = []
    x_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    for data in x_list:
        print("x_0", data)
        it_list.append(new_solve(3, 0.5, data))
    print(it_list)
    myPlot(x_list, it_list, 2)
    # new_solve(3, 1, 0.1)
    plt.show()