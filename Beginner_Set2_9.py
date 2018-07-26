x,n=list(map(int,input().strip().split()))
y=[int(i) for i in input().strip().split()]
s=0
for i in range(n):
	s=s+y[i]
print(s)
