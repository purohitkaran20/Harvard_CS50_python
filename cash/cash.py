def main():
    print(change_coin_num(validate_input()))


def validate_input():
    while True:
        try:
            c = int(input("Change owed: "))
            if c < 0:
                continue
            else:
                return c
        except ValueError:
            continue

def change_coin_num(leftover):
    cents = (25,10,5,1)
    coins_given = 0
    i = 0
    while True:
        if leftover == 0:
            return 0
        elif leftover - cents[i] >= 0:
            leftover = leftover - cents[i]
            coins_given += 1
            if leftover == 0:
                return coins_given
        else:
            i += 1



if __name__=="__main__":
    main()
