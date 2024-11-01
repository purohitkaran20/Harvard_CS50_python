import os
import sys


def validate_arguments(arguments, files):
    if len(arguments) == 1:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    filename = arguments[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")
    if filename not in files:
        sys.exit("File does not exist")


def open_file_count_lines(filename):
    i = 0
    with open(filename) as file:
        for line in file:
            if  line.strip() == "" or line.strip().startswith("#"):
                pass
            else:
                i+=1
    return i


def main():
    files = os.listdir(".")
    arguments = sys.argv
    validate_arguments(arguments, files)
    filename = arguments[1]
    print(open_file_count_lines(filename))


if __name__ == "__main__":
    main()
