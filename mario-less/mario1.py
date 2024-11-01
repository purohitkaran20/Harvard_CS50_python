def main():
    print_pyramid(validate_input())


def validate_input():
    while True:
        try:
            h = int(input("Height: "))
            if h<1 or h>8:
                continue
            else:
                return h
        except ValueError:
            continue

def print_pyramid(h):
    for i in range(1,(h+1)):
        print("#"*i)

if __name__=="__main__":
    main()
