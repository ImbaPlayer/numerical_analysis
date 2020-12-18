# -*- coding: utf-8 -*-
# @Author: Guanglin Duan
# @Date:   2020-12-18 10:12:06
# @Last Modified by:   Guanglin Duan
# @Last Modified time: 2020-12-18 11:23:43
import scipy.linalg as li
import numpy as np
import itertools as it
import math
import matplotlib.pyplot as plt

def f_true(x):
    return np.sqrt(1+2*x)

def f(x, y):
    return y - 2*x/y

def implicit_RK2(x0, y0, h, r):
    x_list = [x0]
    y_list = [y0]
    while x0 < 10:
        K1_0 = f(x0 + r*h, y0)
        for i in range(100):
            K1 = f(x0 + r*h, y0 + r*h*K1_0)
            if np.abs(K1-K1_0) < 1e-5:
                # print("K1", i)
                break
            K1_0 = K1
        K2_0 = f(x0 + (1-r)*h, y0)
        for i in range(100):
            K2 = f(x0 + (1-r)*h, y0 + h*(1-2*r)*K1 + r*h*K2_0)
            if np.abs(K2-K2_0) < 1e-5:
                # print("K2", i)
                break
            K2_0 = K2
        y = y0 + h/2*(K1 +K2)
        y0 = y
        x0 = x0 + h
        
        x_list.append(x0)
        y_list.append(y0)
    return x_list, y_list

def main():
    i = 1
    # r + 向上偏
    # r - 向下偏
    r = 0.5 - np.sqrt(3)/6
    for h in [0.01, 0.1, 0.5]:
        plt.subplot(1,3,i)
        i += 1
        # _, y_xianshi = RK2(0,1,h)
        r = 0.5 + np.sqrt(3)/6
        x_test, y_test = implicit_RK2(0, 1, h, r)
        r = 0.5 - np.sqrt(3)/6
        x_test_, y_test_ = implicit_RK2(0, 1, h, r)
        y_true = f_true(np.array(x_test))
        # plt.figure(figsize=(10,10))
        # plt.plot(x_test, y_rk4, label="RK4")
        plt.plot(x_test, y_test, label="implicit_RK2_r1")
        plt.plot(x_test_, y_test_, label="implicit_RK2_r2")
        plt.plot(x_test, y_true, label="ground")
        plt.title("h={}".format(h))
        plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
