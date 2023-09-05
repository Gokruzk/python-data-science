# Sets

# * Don't record element position
# * Only have unique elements

Set1 = {'pop', 'rock', 'soul', 'rock', 'hard rock', 'rock'}
print(Set1)  # ? {'pop', 'rock', 'soul', 'hard rock'}

# TODO: conver list to set
L = [1, 2, 1, 3, 2]
s = set(L)
print(s)  # ? {1,2,3}

# * Set operations
A = {'Radiohead', 'AC/DC'}

# TODO: add element to set
A.add('NSYNC')
print(A)
A.add('NSYNC')  # ? if we try to add the same element is not added
print(A)  # ? {'NSYNC', 'Radiohead', 'AC/DC'}

# TODO: remove element of set
A.remove('NSYNC')
print(A)

# TODO: check if item is on the set
print('xd' in A)  # ? false
print('Radiohead' in A)  # ? true

B = {'Verde70', 'Equilivre', 'Radiohead'}

# TODO: intersection of two sets
print(A & B)  # ? {'Radiohead'}

# TODO: union of two sets
A.union(B)
print(A)

# TODO: check if set is a subset
C = {'Verde70', 'Radiohead'}
print(C.issubset(B))  # ? true
