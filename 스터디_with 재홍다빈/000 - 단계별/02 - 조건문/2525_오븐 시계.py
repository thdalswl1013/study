a, b = map(int, input().split())
c = int(input())

hour = (b+c)//60
min = (b+c)%60

if (b + c >= 60):
  if (a+hour >= 24):
    a = a - 24
  a = a + hour
  print(a, min)

else:
  if(a >= 24):
    a = a - 24
  print(a, b+c)