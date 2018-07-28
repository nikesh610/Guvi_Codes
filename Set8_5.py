import math
x=list(input())
if(len(x)%2==0):
	a=math.floor(len(x)/2)
	b=a-1
	x[a]="*"
	x[b]="*"
	for i in range(len(x)):
		print(x[i],end="")
else:
	a=math.floor(len(x)/2)	
	x[a]='*'
	for i in range(len(x)):
		print(x[i],end="")
