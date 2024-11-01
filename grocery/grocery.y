d = {}
l = []
while True:
    try:
        i = (input()).upper()
        l.append(i)
    except EOFError:
        break

for i in l:
  if i not in d:
    d[i] = 1
  else:
    d[i] +=1

for key, value in sorted(d.items()):
  print(value, key)
