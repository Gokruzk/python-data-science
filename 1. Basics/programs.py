# hello world
print("Hello\nworld")
print('\n')
# * types
# * integer (int), reals (float), strings(str)

# TODO: convert int to float
print(float(2))

# TODO: convert 1.1 to int
print(int(1.1))

# TODO: convert '1' to int
print(int('1'))

# TODO: convert 1 to str
print(str(1))

# TODO: convert 1.1 to str
print(str(1.1))

# TODO: convert 1 to boolean
print(bool(1))

print('\n')

# * Expressions: Mathematical operations
print(50 + 40 + 10)
print(50 + 40 - 10)
print(5-10)
print(5**2)  # ? pow
print(25/6)
print(25//6)  # ? integer division

print('\n')

# ? Variables
my_v = 1
print(my_v)
x = 43 + 10 * 2
print(x)
y = x / 60
print(y)
x /= 60
print(x)

print('\n')

# ? Strings
name = "Gokruzk"
# TODO: print the last letter
print(name[-1])

# TODO: print the first letter
print(name[-7])

# TODO: store first name and last name in variables
name = "Nigell Jama"
first_name = name[0:6]
last_name = name[7:11]
print(first_name + " " + last_name)  # ? concatenate

# TODO: get lenth of the string
print(len(name))

# TODO: get lenth of the string
print(3 * first_name)

# TODO: hello message with first name
print("Hello " + first_name)

# TODO: escape consequences
print("Hello \n" + first_name)

# TODO: escape consequences
print("Hello \\" + first_name)

# TODO: convert to upper case
print("hello".upper())

# TODO: replace words
my_name = name.replace('Nigell', 'Marcel')
print(my_name)

# TODO: find strings
print(my_name.find('z'))  # ? return 1 if found, return -1 if not found

Numbers = "01234567"
print('1'+'2')
