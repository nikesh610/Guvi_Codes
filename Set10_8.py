x=int(input())
x=[int(i) for i in input().strip().split()]
d=x[1]-x[0]
for i in range(1,len(x)-1):
	if(x[i+1]-x[i]!=d):
		print(x[i]+d)
		break
