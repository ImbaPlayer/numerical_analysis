import numpy as np
def rqrt(n):
    number = np.array([n])
    y = number.astype(np.float32)
    x2 = y*0.5
    i=y.view(np.int32)
    i[:]=0x5f3759df-(i>>1)
    y = y*(1.5-x2*y*y)
    y = y*(1.5-x2*y*y)
    return y
def cal2(n):
    y3 = np.array([n])
    y3 = y3.astype(np.float32)
    x2 = y3*0.5
    ii = y3.view(np.int32)
    ii[:] = 0x5f3759df - (ii >> 1)
    y3 = y3*(1.5-x2*y3*y3)
    y3 = y3*(1.5-x2*y3*y3)
    return y3
if __name__ == "__main__":
    x = np.float32(2)
    print(cal2(2)[0])
    print("right result", 1/np.sqrt(x))
    print(rqrt(x))