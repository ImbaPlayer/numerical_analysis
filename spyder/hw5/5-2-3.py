import numpy as np
import matplotlib.pyplot as plt
import math

eps = 1e-6
maxIter = 50
def p(x, x_list):
    y = 1
    for data in x_list:
        y = y * (x - data)
    return y

def p_d(x, x_list):
    l = len(x_list)
    result = 0
    for i in range(l):
        result += p(x, np.delete(x_list, i))
    return result

def p_d_d(x, x_list):
    l = len(x_list)
    result = 0
    for i in range(l):
        temp_list = np.delete(x_list, i)
        result += p_d(x, temp_list)
    return result

def p_n_m(x, x_list, root_list):
    return p(x, x_list) / p(x, root_list)

def p_n_m_d(x, x_list, root_list):
    a = p_d(x, x_list) * p(x, root_list) - p(x, x_list) * p_d(x, root_list)
    b = (p(x, root_list))
    return a / b

def g(x, x_list, root_list):
    return x + p_n_m(x, x_list, root_list) / p_n_m_d(x, x_list, root_list)

def solve(x_list, root_list, x_0):
    itNum = 0
    err = 1
    result = [x_0]
    while err > eps and itNum <= maxIter:
        x_k = g(x_0, x_list, root_list)
        err = np.abs(x_k - x_0)
        x_0 = x_k
        itNum += 1
        result.append(x_k)
        # if abs(x_k) > 1e5:
        #     print("error", x_k)
        #     return np.inf
    print("itNum", itNum)
    print("err", err)
    print("one iter root", result)

def simple_solve(x_list, x_0):
    itNum = 0
    err = 1
    result = [x_0]
    while err > eps and itNum <= maxIter:
        x_k = x_0 - p(x_0, x_list) / p_d(x_0, x_list)
        err = np.abs(x_k - x_0)
        x_0 = x_k
        itNum += 1
        result.append(x_k)
        if abs(x_k) > 1e5:
            print("error", x_k)
            return np.inf
    print("itNum", itNum)
    print("err", err)
    print("one iter root", result)
    # print("right ans", 1 / b)
    return itNum

# 牛顿法重根的第一种改进
def improve_one(x_list, x_0, m):
    itNum = 0
    err = 1
    result = [x_0]
    while err > eps and itNum <= maxIter:
        x_k = x_0 - m * p(x_0, x_list) / p_d(x_0, x_list)
        err = np.abs(x_k - x_0)
        x_0 = x_k
        itNum += 1
        result.append(x_k)
        if abs(x_k) > 1e5:
            print("error", x_k)
            return np.inf
    print("itNum", itNum)
    print("err", err)
    print("one iter root", result)
    # print("right ans", 1 / b)
    return itNum

# 牛顿法重根的第二种改进
def improve_two(x_list, x_0, m):
    itNum = 0
    err = 1
    result = [x_0]
    while err > eps and itNum <= maxIter:
        x_k = x_0 - (p(x_0, x_list) * p_d(x_0, x_list)) / (p_d(x_0, x_list)**2 - p(x_0, x_list) * p_d_d(x_0, x_list))
        err = np.abs(x_k - x_0)
        x_0 = x_k
        itNum += 1
        result.append(x_k)
        if abs(x_k) > 1e5:
            print("error", x_k)
            return np.inf
    print("itNum", itNum)
    print("err", err)
    print("one iter root", result)
    # print("right ans", 1 / b)
    return itNum
def main():
    x_list = np.array([i * 1.0 for i in range(5, 9)])
    print("root", x_list)
    solve(x_list, [6], 7.9)
    solve(x_list, [6, 7.989205490115172], 6.5)
    solve(x_list, [6, 7.989205490115172, 7.000000334411901], 4.5)

def cal_first_root():
    # x_list = np.array([i * 1.0 for i in range(5, 9)])
    x_list = [5,6,7,7,8]
    print("root", x_list)
    x_0 = 7.4
    # x_0 = 7.3
    simple_solve(x_list, x_0)
    improve_one(x_list, x_0, 2)
    improve_two(x_list, x_0, 2)



if __name__ == "__main__":
    cal_first_root()
    # main()
