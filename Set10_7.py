x=int(input())
s=0
while(x!=0):
	r=x%10
	s=s*10+r
	x=int(x/10)
print(s)
