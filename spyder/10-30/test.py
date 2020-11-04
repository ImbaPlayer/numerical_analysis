import numpy as np

def test():
    a = np.array([1,2,3])
    b = 2 - a
    print(b)
    print(np.prod(b))

if __name__ == "__main__":
    test()