# Conditionals and Branching

# * Comparison operator

print(2 == -2)  # ? false
print(2 == 2)  # ? true
print(5 > 10)  # ? true
print(5 >= 1)  # ? true
print(2 <= 3)  # ? true
print('Radiohead' == 'Oasis')  # ? false

# * Conditionals

# TODO: check if age > 18 to get in to concert elseif age == 18 get into coldplay
age = int(input("What's your age? "))

if (age > 18):
    print('get in')
elif (age == 18):
    print('go see coldplay')
else:
    print('move on')

# * Logic operators

# ? or
x = 3
if (x == 1 or x == 3):
    print('1 o 3')

y = 5
# ? and
if (x == 1 and y == 4):
    print('1 and 4')
else:
    print(f'y = {y}')
