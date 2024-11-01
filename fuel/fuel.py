while True:
  try:
    z = str(input('Fraction: ')).split("/")
    x = int(z[0])
    y = int(z[1])
    if x>y or y==0:
      continue
    else:
      break
  except:
    IndexError or ValueError
    continue

w = round((x/y)*100)
if w<=1:
  print('E')
elif w>=99:
  print("F")
else:
  print(w,"%",sep="")
