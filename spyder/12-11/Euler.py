# -*- coding: utf-8 -*-
# @Author: Guanglin Duan
# @Date:   2020-12-11 09:51:53
# @Last Modified by:   Guanglin Duan
# @Last Modified time: 2020-12-11 12:15:45

import scipy.linalg as li
import numpy as np
import itertools as it
import math
import matplotlib.pyplot as plt

def f_true(x):
    return np.sqrt(1+2*x)

def f(x, y):
    return y - 2*x/y

def solve(x0, y0, h):
    x_list = [x0]
    y_list = [y0]
    while x0 < 10:
        y = y0 + h * f(x0, y0)
        y0 = y
        x0 = x0 + h
        
        x_list.append(x0)
        y_list.append(y0)
    return x_list, y_list

def solve_tixing(x0, y0, h):
    s = 50
    x_list = [x0]
    y_list = [y0]
    while x0 < 10:
        y = y0 + h * f(x0, y0)
        x_next = x0 + h
        for _ in range(s):
            ys = y0 + h/2 * (f(x0, y0) + f(x_next, y))
            if np.abs(ys - y) < 1e-4:
                y = ys
                break
            y = ys
        y0 = ys
        x0 = x_next
        x_list.append(x0)
        y_list.append(y0)
    return x_list, y_list


def main():
    i = 1
    for h in [0.01, 0.1, 0.5]:
        plt.subplot(1,3,i)
        i += 1
        _, y_xianshi = solve(0,1,h)
        x_test, y_test = solve_tixing(0, 1, h)
        print("x", x_test)
        print("y", y_test)
        y_true = f_true(np.array(x_test))
        print(y_true)
        # plt.figure(figsize=(10,10))
        plt.plot(x_test, y_xianshi, label="xianshi")
        plt.plot(x_test, y_test, label="tixing")
        plt.plot(x_test, y_true, label="ground")
        plt.title("h={}".format(h))
        plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
