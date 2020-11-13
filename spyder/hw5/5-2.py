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
    return x_k

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
    return x_k

def main():
    x_list = np.array([i * 1.0 for i in range(5, 9)])
    print("root", x_list)
    solve(x_list, [7], 6.7)
    solve(x_list, [7, 4.999999094063967], 5.7)
    solve(x_list, [7, 4.999999094063967, 5.999999999999999], 8.1)
    # for i in range(10):
    #     j = 8+i*0.1
    #     # solve(x_list, [6], j)
    #     solve(x_list, [6, 7], j)
    # # solve(x_list, [6, 4.999999999999434], 6.9)
    # # solve(x_list, [7, 4.999999094063967, 5.999999999999999], 7.5)

def cal_first_root():
    x_list = np.array([i * 1.0 for i in range(5, 9)])
    print("root", x_list)
    simple_solve(x_list, 6.7)

def get_result():
    x_list = np.array([i * 1.0 for i in range(5, 9)])
    x0_list = []
    x_solve = []
    for i in range(5, 8):
        for j in range(1, 10):
            x0_list.append(i + j * 0.1)
    print(x0_list)
    for data in x0_list:
        x1 = simple_solve(x_list, 5.8)
        for x in x_list:
            if np.abs(x-x1) < eps:
                x_solve.append(x1)
                break
        
        # for data2 in x0_list:
        #     x2 = solve(x_list, x_solve, data2)
        #     for x in x_list:
        #         if np.abs(x-x2) < eps:
        #             x_solve.append(x2)
        #             break
            
        #     for data3 in x0_list:
        #         x3 = solve(x_list, x_solve, data3)
        #         for x in x_list:
        #             if np.abs(x-x3) < eps:
        #                 x_solve.append(x3)
        #                 break
        #         for data3 in x0_list:
        #             x4 = solve(x_list, x_solve, data3)
        #             for x in x_list:
        #                 if np.abs(x-x4) < eps:
        #                     x_solve.append(x4)
        #                     break
                    
if __name__ == "__main__":
    cal_first_root()
    main()
    # get_result()
