
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2<= len(s)<=6 and s[:2].isalpha() and verify_condition3(s):
        return True
    else:
        return False

def verify_condition3(s):
    if s.isalnum():
        pass
    else:
        return False

    if s.isalpha():
        return True
    else:
        pass

    for i,j in enumerate(s):
        if j.isdigit():
            break

    if s[i]== '0':
       return False
    else:
        pass

    sub_s = s[i:]
    k=0
    for i,j in enumerate(sub_s):
        if j.isalpha():
            k+=1
        else:
            pass

    if k==0:
        return True
    else:
        return False
main()
