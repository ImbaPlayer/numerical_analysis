# -*- coding: utf-8 -*-
# @Author: Guanglin Duan
# @Date:   2020-12-18 10:12:06
# @Last Modified by:   Guanglin Duan
# @Last Modified time: 2020-12-25 10:29:12
import scipy.linalg as li
import numpy as np
import itertools as it
import math
import matplotlib.pyplot as plt

def f_true(x):
    return np.sqrt(1+2*x)

def f(x, y):
    return y - 2*x/y

def RK2(x0, y0, h):
    x_list = [x0]
    y_list = [y0]
    while x0 < 10:
        y = y0 + h * f(x0, y0)
        y = y0 + h/2 * (f(x0, y0) + f(x0+h, y))
        y0 = y
        x0 = x0 + h
        
        x_list.append(x0)
        y_list.append(y0)
    return x_list, y_list

def RK4(x0, y0, h):
    x_list = [x0]
    y_list = [y0]
    while x0 < 10:
    # for i in range(3):
        K1 = f(x0, y0)
        K2 = f(x0 + h/2, y0 + h/2 * K1)
        K3 = f(x0 + h/2, y0 + h/2 * K2)
        K4 = f(x0 + h, y0 + h * K2)
        y = y0 + 1/6*h*(K1 + 2*K2 + 2*K3 + K4)
        y0 = y
        x0 = x0 + h
        
        x_list.append(x0)
        y_list.append(y0)
    return x_list, y_list

def Adams(x_list, y_list, h):
    y_adam = y_list[0:4]
    x_adam = x_list
    for i in range(4, len(x_list)):
        temp_y = y_adam[i-1] + h/24*(55*f(x_list[i-1], y_adam[i-1]) - 59*f(x_list[i-2], y_adam[i-2]) +
            37*f(x_list[i-3], y_adam[i-3]) - 9*f(x_list[i-4], y_adam[i-4]))
        y_adam.append(temp_y)
    return x_adam, y_adam


def main():
    i = 1
    for h in [0.01, 0.05, 0.1]:
        plt.subplot(1,3,i)
        i += 1
        x_test, y_test = RK4(0, 1, h)
        x_adam, y_adam = Adams(x_test, y_test, h)
        plt.plot(x_test, y_test, label="RK4")
        y_true = f_true(np.array(x_adam))
        plt.plot(x_adam, y_adam, label="Adam")
        plt.plot(x_adam, y_true, label="ground")
        plt.title("h={}".format(h))
        plt.legend()
    plt.show()

def RK_main():
    i = 1
    for h in [0.01, 0.1, 0.5]:
        plt.subplot(1,3,i)
        i += 1
        # _, y_xianshi = RK2(0,1,h)
        x_test, y_test = RK2(0, 1, h)
        _, y_rk4 = RK4(0, 1, h)
        y_true = f_true(np.array(x_test))
        # plt.figure(figsize=(10,10))
        plt.plot(x_test, y_rk4, label="RK4")
        plt.plot(x_test, y_test, label="RK2")
        plt.plot(x_test, y_true, label="ground")
        plt.title("h={}".format(h))
        plt.legend()
    plt.show()




if __name__ == "__main__":
    main()
