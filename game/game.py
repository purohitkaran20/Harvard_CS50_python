import random

while True:
  try:
    l = int(input("Level: "))
    if l > 0:
      break
    else:
      continue
  except:
    ValueError

r = random.randint(1,l)

while True:
  try:
    g = int(input("Guess: "))
    if g < 0:
      continue
    elif g < r:
      print("Too small!")
      continue
    elif g > r:
      print("Too large!")
      continue
    else:
      print("Just right!")
      break
  except:
    ValueError
