# Open files with open function

# ? Create a file object {r: reading, w: writing}
File = open("./example.txt", "r")

# TODO: print file name
print(File.name)

# TODO: print file mode
print(File.mode)  # ? r

# TODO: close file
File.close()

with open("./example.txt", "r") as File1:
    file_stuff = File1.read()  # ? store the content of the file
    print(file_stuff)  # ? Hello world xd

print(File1.closed)  # ? check if the file is closed ? true
print(file_stuff)

print('\n')

with open("./example.txt", "r") as File1:
    file_stuff = File1.readlines()  # ? store the lines of the file in a list
    print(file_stuff)  # ? ['Hello world\n', 'xd']

print('\n')

with open("./example.txt", "r") as File1:
    file_stuff = File1.readline()  # ? print the first line
    print(file_stuff)  # ? Hello world
    file_stuff = File1.readline()  # ? print the second line
    print(file_stuff)  # ? xd
    # ? and so on...

print('\n')

# TODO: print every line with loop
with open("./example.txt", "r") as File1:
    for line in File1:
        print(line)

print('\n')

# TODO: print the first n charecters of a line
with open("./example.txt", "r") as File1:
    file_stuff = File1.readline()
    print(file_stuff[:2])  # ? He
    file_stuff = File1.readline()
    print(file_stuff[:1])  # ? x
