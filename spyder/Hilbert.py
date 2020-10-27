import numpy as np

def Hilbert(n):
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i,j] = np.float64(1.0 / (i + j + 1))
    return A

# ord = 1, 2, np.inf
def Cond(A, ord):
    A_inv = np.linalg.inv(A)
    A_norm = np.linalg.norm(A, ord=ord)
    A_inv_norm = np.linalg.norm(A, ord=ord)
    cond = A_norm * A_inv_norm
    return cond

def mySolve(A, b):
    print("mySolve float64")
    Ab = np.c_[A,b]
    # print(Ab)
    for i in range(n):
        a = Ab[i,i]
        for j in range(i + 1, n):
            l = Ab[j,i] / a
            Ab[j] += -l * Ab[i]
        # print(Ab)
    d = Ab[:,n]
    x = np.zeros(n)
    x[n-1] = d[n-1] / Ab[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = (d[i] - np.inner(Ab[i, i+1:n], x[i + 1:n])) / Ab[i,i]
    return x

def X_Error(x, x_e):
    return np.linalg.norm(x_e - x, ord=2) / np.linalg.norm(x, ord=2)

def Error_Range(A, x_e, b):
    r = b - np.dot(A, x_e)
    a = (1 / Cond(A, 2)) * np.linalg.norm(r, ord=2) / np.linalg.norm(b, ord=2)
    b = Cond(A, 2) * np.linalg.norm(r, ord=2) / np.linalg.norm(b, ord=2)
    print("Error range", a, b)

def SolveHilbert(n):
    A = Hilbert(n)
    print("%d Hilbert's cond: %f" % (n, Cond(A, 2)))
    xTrue = np.random.randn(n)
    b = np.inner(A,xTrue)
    # A = np.float32(A)
    # xTrue = np.float32(xTrue)
    # b = np.float32(b)

    xGauss = mySolve(A, b)
    print("x relative error", X_Error(xTrue, xGauss))
    xGauss = np.linalg.solve(A, b)
    # xGauss = np.float32(xGauss)

    print("xTrue", xTrue)
    print("xGauss", xGauss)
    # print(xTrue[0])
    # print(xGauss[0])
    print("x relative error", X_Error(xTrue, xGauss))
    Error_Range(A, xGauss, b)

    noise = 0.00001
    # add noise to A
    A[0, 0] += noise
    # b = np.inner(A,xTrue)

    xGauss = mySolve(A, b)

    print("xTrue", xTrue)
    print("xGauss", xGauss)
    print("x relative error", X_Error(xTrue, xGauss))
    Error_Range(A, xGauss, b)

    # add noise to b
    A = Hilbert(n)
    b = np.inner(A,xTrue)
    b[0] += noise
    xGauss = mySolve(A, b)

    print("xTrue", xTrue)
    print("xGauss", xGauss)
    print("x relative error", X_Error(xTrue, xGauss))
    Error_Range(A, xGauss, b)

def test():
    x_e = np.array([1,2])
    x = np.array([1,2])
    a = np.linalg.norm(x_e - x, ord=2) / np.linalg.norm(x, ord=2)
    print("test", X_Error(x, x_e))

if __name__ == "__main__":
    # for i in range(2, 21):
    #     H = Hilbert(i)
    #     print("%d Hilbert's cond: %f" % (i, Cond(H, 2)))
    n = 7
    SolveHilbert(n)

    # test()