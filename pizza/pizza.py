import os
import sys
import csv
from tabulate import tabulate

def validate_arguments(arguments, files):
    if len(arguments) == 1:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    filename = arguments[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")
    if filename not in files:
        sys.exit("File does not exist")


def convert_to_ascii(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))

def main():
    arguments = sys.argv
    files = os.listdir(".")
    validate_arguments(arguments, files)
    filename = arguments[1]
    print(convert_to_ascii(filename))

if __name__ == "__main__":
    main()

