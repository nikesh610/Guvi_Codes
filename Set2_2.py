x=int(input())
t1=x
t2=0
while(x>0):
  r=x%10
  t2=t2*10+r
  x=int(x/10)
if(t2==t1):
  print("yes")
else:
  print("no")
