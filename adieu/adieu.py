a = 'Adieu, adieu, to '

l = []
try:
  while True:
    i = str(input("Input: "))
    l.append(i)
except:
  EOFError

l1 = l[:-1]
print(l1)
l2 = l[-1]
print(l2)
l1s = ', '.join(l1)
print(l1s)
c = ", and "
if len(l) == 1:
  print(a+l2 )
elif len(l)==2:
  print(a+l1s+" and "+l2)
else:
  print(a + l1s + c + l2)
