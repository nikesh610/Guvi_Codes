a,b=map(int,input().strip().split())
temp1=a*b
while(b>0):
	r=a%b
	a=b
	b=r
print(int(temp1/a))
