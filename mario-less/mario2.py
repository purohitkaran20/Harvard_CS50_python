from mario1 import validate_input

def main():
    print_pyramid(validate_input())


def print_pyramid(h):
    for i in range(1,(h+1)):
        print(' '*(h-i), '#'*i, " ", '#'*i, ' '*(h-i))

if __name__=="__main__":
    main()
