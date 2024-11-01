def main():
    string = input("What time is it?\n")
    t = convert(string)

    if 7.00 <= t <= 8.00:
        print('breakfast time')
    elif 12.00 <= t <= 13.00:
        print('lunch time')
    elif 18.00 <= t <= 19.00:
        print('dinner time')
    else:
        pass

def convert(time):
    x,y = map(float, time.split(':'))
    z = y*(1/60)
    return x+z

if __name__ == "__main__":
    main()
