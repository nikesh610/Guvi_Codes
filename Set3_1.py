n,a,d=map(int,input().strip().split())
s=0
for i in range(n):
	s=s+a
	a=a+d
print(s)
