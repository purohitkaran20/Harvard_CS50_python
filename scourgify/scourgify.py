import os
import sys
import csv


def validate_arguments(arguments, files):
    if len(arguments) < 3:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 3:
        sys.exit("Too many command-line arguments")
    before = arguments[1]
    after = arguments[2]
    if not before.endswith(".csv") and after.endswith(".csv"):
        sys.exit("Not a CSV file")
    if before not in files:
        sys.exit(f"Could not read {before}")


def clean_data(before, after):
    with open(before) as input:
        reader = csv.reader(input)
        next(reader) # skip header
        data = list(reader)

    with open(after, mode='w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(["first", "last", "house"])
        for row in data:
            name = row[0].split(",")
            name[0], name[1] = name[1].strip(), name[0].strip()
            writer.writerow(name + row[1:])


def main():
    arguments = sys.argv
    files = os.listdir(".")
    validate_arguments(arguments, files)
    before = arguments[1]
    after = arguments[2]
    clean_data(before, after)

if __name__ == "__main__":
    main()

