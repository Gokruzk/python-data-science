# Functions

def main():
    L = [10, 8, 6, 7, 5]
    print(len(L))  # ? 5
    print(sum(L))  # ? sum: 36
    sortedL = sorted(L)  # ? create other list
    print(sortedL)  # ? [5,6,7,8,10]
    L.sort()  # ? works in the same list
    print(L)  # ? [5,6,7,8,10]
    print(sum1(2))

    print('\n')

    BandNames('Radiohead', 'Oasis')
    BandNames('Radiohead', 'Oasis', 'Coldplay')


def sum1(x):
    """
        add 1 to x
    """
    return int(x + 1)


def mult(a, b):
    return a * b

# ? *parameter is for receive n paramenters


def BandNames(*names):
    for name in names:
        print(name)


main()
