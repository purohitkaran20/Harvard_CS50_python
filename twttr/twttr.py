# x = input("Enter text: ")
# x = x.lower()
# for y in x:
#     if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u':
#         pass
#     else:
#         print(y, end="")


# input = input("Enter text: ").lower()
# vowels = 'aeiou'
# print(''.join([i for i in input if i not in vowels]))



vowels = 'aeiouAEIOU'
def main():
    print(shorten(input("Enter text: ")))

def shorten(word):
    return ''.join([i for i in word if i not in vowels])

if __name__ == "__main__":
    main()
