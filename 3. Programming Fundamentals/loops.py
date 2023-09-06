# Loops

# * For

squares = ['white', 'yellow', 'green', 'violet', 'blue']

# TODO: print elements in the list
for i in range(0, 5):
    print(squares[i])

print('\n')

# TODO: print elements in the list without range
for square in squares:
    print(square)

print('\n')

# TODO: print elements in the list with its indexs
for i, square in enumerate(squares):
    print(f'{i}. {square}')

print('\n')

# * While

squares = ['white', 'yellow', 'green', 'green', 'blue']
newSquares = []

i = 0
while (squares[i] != 'green'):
    newSquares.append(squares[i])
    i += 1

print(newSquares)  # ? ['white', 'yellow']
