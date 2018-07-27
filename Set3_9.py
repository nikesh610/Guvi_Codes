import math
x=list(map(int,input().strip().split()))
y=list(map(int,input().strip().split()))
x1=x[0]*60+x[1]
y1=y[0]*60+y[1]

if(y1>=x1):
	z=y1-x1
	print(math.floor(z/60),z%60)
else:
	z=x1-y1
	print(math.floor(z/60),z%60)
