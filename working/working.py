import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    start_hour, start_minute, start_meridiem, end_hour, end_minute, end_meridiem = validate_input(s)
    start = get_start_time_24(start_hour, start_minute, start_meridiem)
    end = get_end_time_24(end_hour, end_minute, end_meridiem)
    return f"{start} to {end}"


def validate_input(s):
    if match := re.search(r"^(?P<start_hour>[1-9]|1[0-2]):?(?P<start_minute>[0-5][0-9])? (?P<start_meridiem>AM|PM) to (?P<end_hour>[1-9]|1[0-2]):?(?P<end_minute>[0-5][0-9])? (?P<end_meridiem>AM|PM)$", s):

        start_hour = match.group("start_hour")
        if match.group("start_minute") == None:
            start_minute = '00'
        else:
            start_minute = match.group("start_minute")
        start_meridiem = match.group("start_meridiem")

        end_hour = match.group("end_hour")
        if match.group("end_minute") == None:
            end_minute = '00'
        else:
            end_minute = match.group("end_minute")
        end_meridiem = match.group("end_meridiem")
        return start_hour, start_minute, start_meridiem, end_hour, end_minute, end_meridiem

    else:
        raise ValueError

def get_start_time_24(start_hour, start_minute, start_meridiem):
    if len(start_hour) == 1:
        start_hour = '0'+start_hour

    if start_hour == '12' and start_meridiem == 'AM':
        start_hour = '00'
        start_time_24 = f"{start_hour}:{start_minute}"
        return start_time_24
    elif start_meridiem == 'AM':
        start_time_24 = f"{start_hour}:{start_minute}"
        return start_time_24
    elif start_hour == '12' and start_meridiem == 'PM':
        start_time_24 = f"{start_hour}:{start_minute}"
        return start_time_24
    elif start_meridiem == 'PM':
        start_hour = int(start_hour)+int(12)
        start_time_24 = f"{start_hour}:{start_minute}"
        return start_time_24


def get_end_time_24(end_hour, end_minute, end_meridiem):
    if len(end_hour) == 1:
        end_hour = '0'+end_hour

    if end_hour == '12' and end_meridiem == 'AM':
        end_hour = '00'
        end_time_24 = f"{end_hour}:{end_minute}"
        return end_time_24
    elif end_meridiem == 'AM':
        end_time_24 = f"{end_hour}:{end_minute}"
        return end_time_24
    elif end_hour == '12' and end_meridiem == 'PM':
        end_time_24 = f"{end_hour}:{end_minute}"
        return end_time_24
    elif end_meridiem == 'PM':
        end_hour = int(end_hour)+int(12)
        end_time_24 = f"{end_hour}:{end_minute}"
        return end_time_24


if __name__ == "__main__":
    main()
