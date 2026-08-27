def read_line(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip("\n"))


read_line("data/file1.txt")
# some sample input
# another line
# one more line


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        print(file.readlines())

read_file("data/file1.txt")
# ['some sample input\n', 'another line\n', 'one more line']