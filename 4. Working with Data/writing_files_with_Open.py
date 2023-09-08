# Writing Files with Open

def main():
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    path = "./example.txt"
    path2 = "./example2.txt"
    # writeFile(path)
    write_n_lines(path, lines)
    file1_to_file2(path, path2)


def writeFile(path):
    with open(path, "w") as File:
        File.write("1 line\n")
        File.write("2 line\n")


def write_n_lines(path, lines):
    with open(path, "w") as File:
        for line in lines:
            File.write(line)


def file1_to_file2(path1, path2):
    with open(path1, "r") as readFile:
        with open(path2, "w") as writeFile:
            for line in readFile:
                writeFile.write(line)


main()
