str = input('Expression: ')
list = str.split()

x = float(list[0])
y = float(list[2])

if list[1] == '+':
    print(f'{x+y:.1f}')
elif list[1] == '-':
    print(f'{x-y:.1f}')
elif list[1] == '*':
    print(f'{x*y:.1f}')
elif list[1] == '/':
    print(f'{x/y:.1f}')
