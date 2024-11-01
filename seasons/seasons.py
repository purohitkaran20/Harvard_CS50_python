from datetime import date, time, datetime, timedelta
import inflect
import sys

def main():
    dob = input("Date of Birth: ")
    valid_dob = validate_dob(dob)
    # print(f"user dob: {valid_dob}")
    age_min = cal_age_in_min(valid_dob)
    # print(f"Age in min: {age_min}")
    print(num_to_words(age_min))

def validate_dob(dob):
    try:
        user_date = datetime.strptime(dob, "%Y-%m-%d")
        return user_date
    except ValueError:
        sys.exit("Invalid date")

def cal_age_in_min(valid_dob):
    now = datetime.now().date()
    times = time(0,0,0)
    now_datetime = datetime.combine(now,times)
    # print(f"current time: {now_datetime}")
    age = now_datetime - valid_dob
    # print(f"Age(time delta): {age} ")
    return int(age.total_seconds() / 60)

def num_to_words(age_min):
    p = inflect.engine()
    return p.number_to_words(age_min).replace(" and ", " ").capitalize() + " minutes"


if __name__ == "__main__":
    main()
