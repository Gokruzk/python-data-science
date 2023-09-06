# Dictionaries

# * Dictionaries has keys and values
# ? {key:value, key:value}
dict = {'Radiohead': 'Thinking about you', 'Coldplay': 'Yellow'}

# TODO: add element to dictionary
dict['Oasis'] = 'Talk tonight'
print(dict)

# TODO: add element to dictionary
dict['Oasis'] = 'Talk tonight'
print(dict)

# TODO: delete element from dictionary
del (dict['Oasis'])
print(dict)  # ? {'Radiohead': 'Thinking about you', 'Coldplay': 'Yellow'}

# TODO: check if an element is on the dictionary
print('Oasis' in dict)  # ? false

# TODO: print all the keys of the dictionary
print(dict.keys())

# TODO: print all the values of the dictionary
print(dict.values())

D = {'a':0,'b':1,'c':2}

L = ['c']
L.append(['a','b'])

print(L)