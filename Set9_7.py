a,b=map(int,input().strip().split())
while(b>0):
	r=a%b
	a=b
	b=r
print(a)
