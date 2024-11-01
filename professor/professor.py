import random

def main():
    l = get_level()
    s = 0
    for n in range(0,10):
      x = generate_integer(l)
      y = generate_integer(l)
      cans = x + y
      for i in range(0,3):
        gans = int(input(f'{x} + {y} = '))
        if cans == gans:
          s+=1
          break
        else:
          print("EEE")
      print(f'{x} + {y} = {cans}')

    print(f"Score: {s}")



def get_level():
    while True:
      try:
        level = int(input("Level: "))
        if level in [1,2,3]:
          return level
        else:
          continue
      except:
        ValueError

def generate_integer(level):
    if level == 1:
      return random.randint(0,9)
    elif level == 2:
      return random.randint(10,99)
    else:
      return random.randint(100,999)

if __name__ == "__main__":
    main()
