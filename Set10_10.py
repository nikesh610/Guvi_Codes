x=int(input())
s=1
while(x!=0):
	r=x%10
	s=s*r
	x=int(x/10)
print(s)	
