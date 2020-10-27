import numpy as np
import matplotlib.pyplot as plt
import math

e = 1e-6
def f1(x):
    return x**3 - 11.1*x**2 + 38.8*x - 41.77

def f2(x):
    return 1 - x - x**2/8.0 + x**3/64.0 + x**4/1536.0

def myPlot():
    x = np.arange(0, 2, 0.1)
    y = f2(x)
    plt.figure(figsize=(10,4))
    plt.plot(x, y)
    plt.show()

def solve(a, b):
    k = math.log((b - a)/e, 2)
    print("k = ", int(k + 1))
    for _ in range(int(k + 1)):
        temp = (b + a) / 2.0
        print("x = ", temp)
        if f2(a) * f2(temp) < 0:
            b = temp
        elif f2(temp) * f2(b) < 0:
            a = temp
        else:
            print(" = 0", temp)
            break
    print("[a, b]", a, b)
    print("x = ", temp)
    print("y = ", f2(temp))
if __name__ == "__main__":
    # myPlot()
    solve(0, 1)