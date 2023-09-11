# Numpy 1D Arrays

# * Numpy array is similar to a list. It's usually fixed in size and each element is of the same type


import numpy as np


def main():
    arr = [0, 1, 2, 3, 4, 5]
    a = np.array(arr)
    print(a)
    print(type(a))
    print(a.dtype)
    print(a.size)

    a[0] = 3
    print(a)  # ? [3,1,2,3,4,5]
    b = a[2:5]
    print(b)  # ? [2,3,4]
    b[1:3] = 20, 30
    print(b)  # ? [2,20,30]

    # * addition and substractions of arrays
    u = np.array([1, 0])
    v = np.array([0, 1])
    z = u + v
    print(z)
    z = u - v
    print(z)

    # * multiplication with a scalar
    y = np.array([1, 2])
    z = 2 * y
    print(z)

    # * product of two numpy arrays
    u = np.array([1, 2])
    v = np.array([3, 2])
    z = u * v
    print(z)

    # * add constant to an numpy array
    u = np.array([1, 2, 3, -1])
    z = u + 1
    print(z)

    # * average
    u = np.array([1, -1, 1, -1])
    z = u.mean()  # ? 0
    print(z)

    v = np.array([1, -2, -3, 4, 5])
    z = v.max()  # ? 5
    print(z)

    # * PI
    x = np.array([0, np.pi/2, 3])  # ? [0, pi/2, 3]
    z = np.sin(x)

    # * intervals
    u = np.linspace([-2, 2], 5)

    print(np.dot(np.array([1,-1]),np.array([1,1])))


if __name__ == "__main__":
    main()
