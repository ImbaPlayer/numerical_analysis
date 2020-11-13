# -*- coding: utf-8 -*-
# @Author: Guanglin Duan
# @Date:   2020-11-13 10:40:01
# @Last Modified by:   Guanglin Duan
# @Last Modified time: 2020-11-13 11:02:08
import numpy as np
import matplotlib.pyplot as plt
import math

x_list = [0.9,1.3,1.9,2.1,2.6,3.0,3.9,4.4,4.7,
            5.0,6.0,7.0,8.0,9.2,10.5,11.3,11.6,12.0,
            12.6,13.0,13.3]
y_list = [1.3,1.5,1.85,2.1,2.6,2.7,2.4,2.15,2.05,
            2.1,2.25,2.3,2.25,1.95,1.4,0.9,0.7,0.6,
            0.5,0.4,0.25]

def find_x(x, x_list):
    for i in range(len(x_list)-1):
        if x > x_list[i] and x < x_list[i + 1]:
            return i

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

# def f_d(i):
    # return y_list[i + 1] - y_list[i]

def Hermit(x, d):
    for i in range(len(x_list)):
        if x == np.array(x_list[i]):
            return y_list[i]
    index = find_x(x, x_list)
    result = f(x, x_list[index], x_list[index+1], y_list[index], y_list[index + 1], d, d)
    return result

def main():
    x_test = np.linspace(0.9,13.3,125)
    # y_test = Hermit(x_test)
    y_test = [Hermit(i, 0) for i in x_test]
    y_test_1 = [Hermit(i, 1) for i in x_test]
    
    plt.plot(x_test, y_test, c="g")
    plt.plot(x_test, y_test_1, c="b")
    plt.scatter(x_list, y_list,c="r")
    # plt.title("n = {}".format(len(x_list)), fontsize=20)
    plt.show()


if __name__ == "__main__":
    main()
