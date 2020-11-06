# -*- coding: utf-8 -*-
# @Author: Guanglin Duan
# @Date:   2020-11-06 11:13:04
# @Last Modified by:   Guanglin Duan
# @Last Modified time: 2020-11-06 11:48:42

import numpy as np
import matplotlib.pyplot as plt
import math

eps = 1e-6
maxIter = 50
x_list = [0.9,1.3,1.9,2.1,2.6,3.0,3.9,4.4,4.7,
            5.0,6.0,7.0,8.0,9.2,10.5,11.3,11.6,12.0,
            12.6,13.0,13.3]
y_list = [1.3,1.5,1.85,2.1,2.6,2.7,2.4,2.15,2.05,
            2.1,2.25,2.3,2.25,1.95,1.4,0.9,0.7,0.6,
            0.5,0.4,0.25]
def p(x, x_list):
    y = 1
    for data in x_list:
        y = y * (x - data)
    return y

def p_no_i(x, x_list, i):
    y = 1
    new_list = np.delete(x_list, i)
    for data in new_list:
        y = y * (x - data)
    return y

def l(x, x_list, i):
    a = p_no_i(x, x_list, i)
    x_i = x_list[i]
    b = p_no_i(x_i, x_list, i)
    return a / b

def L(x, x_list, y_list):
    # for i in range(len(x_list)):
    #     if x_list[i] == x:
    #         return x_list[i]
    length = len(x_list)
    result = 0
    for i in range(length):
        result += y_list[i] * l(x, x_list, i)
    return result


def p_d(x, x_list):
    l = len(x_list)
    result = 0
    for i in range(l):
        result += p(x, np.delete(x_list, i))
    return result

def test(x_list, y_list, k):
    plt.subplot(2,1,k)
    # plt.figure(figsize=(10,10))
    x_test = np.linspace(0.9,13.3,125)
    y_test = L(x_test, x_list, y_list)
    
    plt.plot(x_test, y_test, c="g")
    plt.scatter(x_list, y_list)
    plt.title("n = {}".format(len(x_list)), fontsize=20)
def main():
    plt.figure(figsize=(5,10))
    global x_list, y_list
    test(x_list, y_list, 1)
    remove_list = list(range(0,22,2))
    print(remove_list)
    x_new = []
    y_new = []
    for i in remove_list:
        x_new.append(x_list[i])
        y_new.append(y_list[i])
    test(x_new, y_new, 2)
    plt.show()

if __name__ == "__main__":
    main()
