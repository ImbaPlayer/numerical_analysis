# -*- coding: utf-8 -*-
# @Author: Guanglin Duan
# @Date:   2020-11-13 09:58:13
# @Last Modified by:   Guanglin Duan
# @Last Modified time: 2020-11-13 10:29:54

import numpy as np
import matplotlib.pyplot as plt
import math

def a_0(x, x_0, x_1):
    return (1+2*(x-x_0)/(x_1-x_0))*((x-x_1)/(x_0-x_1))**2

def a_1(x, x_0, x_1):
    return (1+2*(x-x_1)/(x_0-x_1))*((x-x_0)/(x_1-x_0))**2

def b_0(x, x_0, x_1):
    return (x-x_0)*((x-x_1)/(x_0-x_1))**2

def b_1(x, x_0, x_1):
    return (x-x_1)*((x-x_0)/(x_1-x_0))**2

def f(x, x_0, x_1, f_0, f_1, f_d_0, f_d_1):
    return f_0 * a_0(x, x_0, x_1) + f_1 * a_1(x, x_0, x_1) + f_d_0 * b_0(x, x_0, x_1) + f_d_1 * b_1(x, x_0, x_1)

def main():
    x = np.linspace(0,np.pi,50)
    y = f(x, 0, np.pi/2, 0, 1, 1, 0)
    y_true = np.sin(x)
    plt.figure(figsize=(5,5))
    plt.plot(x, y, label='Hermit')
    plt.plot(x, y_true, label='sin(x)')
    plt.legend(loc=3) 
    plt.show()
    max_error = np.max(np.abs(y - y_true))
    print("max error", max_error)
if __name__ == "__main__":
    main()
