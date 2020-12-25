# -*- coding: utf-8 -*-
# @Author: Guanglin Duan
# @Date:   2020-12-25 10:30:22
# @Last Modified by:   Guanglin Duan
# @Last Modified time: 2020-12-25 10:58:29
import scipy.linalg as li
import numpy as np
import itertools as it
import math
import matplotlib.pyplot as plt

l1 = -0.1
l2 = -20
def f_true(l, x):
    return np.exp(l*x)

def f(y):
    L = np.zeros((2,2))
    L[0,0] = l1
    L[1,1] = l2
    return np.inner(L, y)

def solve(x0, y0, h):
    x_list = [x0]
    y_list = y0
    while x0 < 10:
        y = y0 + h * f(y0)
        y0 = y
        x0 = x0 + h
        
        x_list.append(x0)
        # y_list.append(y0)
        y_list = np.c_[y_list, y0]
    return x_list, y_list



def main():
    i = 1
    for h in [0.01, 0.1, 0.5]:
        plt.subplot(1,3,i)
        i += 1
        y0 = np.array([1,1])
        x0 = 0
        x_list, y_list = solve(x0, y0, h)
        # print(x_list)
        # print(y_list)
        y_true_1 = f_true(l1, np.array(x_list))
        y_true_2 = f_true(l2, np.array(x_list))
        plt.plot(x_list, y_list[0,:], label="y1")
        plt.plot(x_list, y_list[1,:], label="y2")
        plt.plot(x_list, y_true_1, label="y1_true")
        plt.plot(x_list, y_true_2, label="y2_true")
        plt.title("Euler h={}, l1={}, l2={}".format(h, l1, l2))
        plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
