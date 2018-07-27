import math
n=int(input())
x=list(map(int,input().strip().split()))
x=sorted(x)
if(len(x)%2==0):
	a=len(x)/2
	b=a+1
	print((x[a]+x[b])/2)
else:
	print(x[math.floor(len(x)/2)])
