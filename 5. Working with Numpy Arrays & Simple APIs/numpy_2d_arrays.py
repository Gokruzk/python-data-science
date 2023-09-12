# Numpy 2D Arrays

import numpy as np


def main():

    a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
    A = np.array(a)
    print(A)
    print(A.ndim)  # ? 2
    print(A.shape)  # ? 3 x 3
    print(A.size)  # ? 3 x 3 = 9

    print("\n")

    # TODO: print the first row
    print(A[0:1])  # ? [row:row]

    print("\n")

    # TODO: print the first row
    print(A[0, 0:3])  # ? [row,column:column]

    print("\n")

    # * Addition of matrix
    X = np.array([[1, 0], [0, 1]])
    Y = np.array([[2, 1], [1, 2]])
    Z = X + Y
    print(Z)

    print("\n")

    # * Multiply by scalar
    Z = 2 * Y
    print(Z)

    print("\n")

    # * Hardmart product
    z = X * Y
    print(z)

    print("\n")

    # * Dot multiplication
    A = np.array([[0, 1, 1], [1, 0, 1]])
    B = np.array([[1, 1], [1, 1], [-1, 1]])
    Z = np.dot(A, B)
    print(Z)


if __name__ == "__main__":
    main()
