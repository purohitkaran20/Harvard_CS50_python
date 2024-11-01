m = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

while True:
  x = input('Date: ').strip().lower()
  if '/' in x:
    x = x.split("/")
    if x[0].isalpha():
      continue
    elif 0<int(x[0])<13 and 0<int(x[1])<32 and int(x[2])>0:
      if len(x[0])==1:
        x[0] = '0'+x[0]
      if len(x[1])==1:
        x[1]='0'+x[1]
      break
    else:
      continue

  elif ',' in x:
    x = x.replace(",",'').split(" ")
    if x[0] in m and 0 < int(x[1]) < 32 and int(x[2]) > 0:
      for i in m:
        if x[0] == i:
           x[0]=str(m.index(i)+1)
           if len(x[0])==1:
             x[0] = '0'+x[0]
      if len(x[1])==1:
        x[1] = '0'+x[1]
      break
  else:
    continue


x.insert(0, x.pop())
date = "-".join(x)
print(date)
