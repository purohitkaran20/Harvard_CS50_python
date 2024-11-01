def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d1 = float(d.replace('$',''))
    return round(d1,2)


def percent_to_float(p):
    p1 = float(p.replace('%',''))
    return round(p1*0.01,2)

main()
