import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'src="(.*?)"' ,s ,re.IGNORECASE):
        url = match.group(1)

        if code := re.search(r"^https?\://(www\.)?youtube.com/embed/(.*)" ,url ,re.IGNORECASE):
            code = code.group(2)
            return f"https://youtu.be/{code}"


if __name__ == "__main__":
    main()
