# Tuples and Lists

# * Tuples are inmutable
tuple1 = ('disk', 10, 1.2)
tuple2 = tuple1 + ('bar', 5, 3)
print(tuple2)

# TODO: get first three elements
print(tuple2[0:3])

# TODO: get rest elements
print(tuple2[3:5])

# TODO: sort list
Rates = (10, 9, 6, 5, 10, 8, 9, 6, 2)
SortedRates = sorted(Rates)
print(SortedRates)

# * Nesting

NT = (1, 2, ('pop', 'rock'), (3, 4), ('disco', (1, 2)))
print(NT[2][0])  # ? pop
print(NT[4][1][1])  # ? 2

print('\n')

# * Lists are mutable
L = ['Mike', 2.3, 4, [1, 2], ('Jack', 7)]

# TODO: get the last item of the list
print(L[-1])

# TODO: slice the last two elements of the list
print(L[3:5])

# TODO: add elements to the list
L1 = L + ['pop', 10]
print(L1)

# TODO: add elements to the same list
L.extend(['pop', 10])  # ? [...,'pop', 10]
print(L)

# TODO: add two elements like one element to the same list
L.append(['rock', 'soft'])  # ? [..,['rock','soft']]
print(L)

# TODO: delete the first element of list
del (L[0])
print(L)

# TODO: convert string to list
LS = "welcome to this lesson".split()
print(LS)

# TODO: convert string to list with specific character
LS = "1,2,3,4".split(',')
print(LS)

# * both variables reference the same list
A = ["hola", 1]
B = A
B[0] = "mundo"
print(A)  # ? ['mundo', 1]

# * clone lists: the variables don't reference the same list
A = ["hola", 1]
B = A[:]
A[0] = "mundo"
print(B)  # ? ['hola', 1]

B = ["a", "b", "c"]
print(B[1:])
