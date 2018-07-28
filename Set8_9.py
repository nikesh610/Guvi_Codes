import math
a,b=map(int,input().strip().split())
x=math.sqrt(a*b)
if(x==int(x)):
	print("yes")
else:
	print("no")
