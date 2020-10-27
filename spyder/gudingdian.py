import numpy as np
import matplotlib.pyplot as plt
import math

eps = 1e-6
maxIter = 50
def f(x):
    return (x + 2.0 / x) / 2.0

def myPlot():
    x_k = 1
    result = [x_k]
    for i in range(10):
        x_k = f(x_k)
        result.append(x_k)
    print(result)
    x = np.arange(0, 11, 1)
    y = np.array(result)
    plt.figure(figsize=(10,4))
    plt.plot(x, y)
    plt.show()

def g(x, a):
    return (x + a/x) / 2

def mySqrt(a):
    itNum = 0
    x_0 = 100
    err = 1
    result = [x_0]
    while err > eps and itNum <= maxIter:
        x_k = g(x_0, a)
        err = np.abs(x_k - x_0)
        x_0 = x_k
        itNum += 1
        result.append(x_k)
    print("itNum", itNum)
    print("err", err)
    print("sqrt({})".format(a), result)
    print("right ans", np.sqrt(a))
if __name__ == "__main__":
    mySqrt(2)
    mySqrt(7)