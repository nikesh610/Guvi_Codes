n=int(input())
if(n==1 or n==0):
	print('1')
elif(n==2):
	print('2')
else:
	s=1
	for i in range(2,n+1):
		s=s*i
	print(s)
 
