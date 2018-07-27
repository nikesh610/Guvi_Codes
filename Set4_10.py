n=int(input())
if(n==1):
	print('1')
elif(n==2):
	print('1 1')
else:
	a=1
	b=1
	print(a,b,end=" ")
	for i in range(n-2):
		c=a+b
		print(c,end=" ")
		a=b
		b=c
