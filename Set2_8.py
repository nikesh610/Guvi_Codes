x,y=map(int,input().strip().split())
for i in range(x+1,y):
	temp=i
	s=0
	while(temp!=0):
		r=temp%10
		s=s+r*r*r
		temp=int(temp/10)
	if(s==i):
		print(i,end=" ")
