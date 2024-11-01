import sys
import pyfiglet
import random

arg = sys.argv
lf = pyfiglet.FigletFont.getFonts()

if len(arg) == 2:
    sys.exit("Invalid usage")
elif len(arg) > 3:
    sys.exit("Invalid usage")
else:
    pass

if len(arg) == 1:
    i = str(input("Input: "))
    f = pyfiglet.Figlet(font=random.choice(lf))
    print(f.renderText(i))
elif str(arg[1]) != '-f' and '--font':
    sys.exit("Invalid usage")
elif str(arg[2]) not in lf:
    sys.exit("Invalid usage")
else:
    i = str(input("Input: "))
    f = pyfiglet.Figlet(font=arg[2])
    print(f.renderText(i))
