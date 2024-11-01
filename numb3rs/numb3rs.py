import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(([0-1]?[0-9]?[0-9]|[2]?[0-4]?[0-9]|[2]?[5]?[0-5])\.){3}([0-1]?[0-9]?[0-9]|[2]?[0-4]?[0-9]|[2]?[5]?[0-5])$"
    if match := re.search(pattern, ip):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
