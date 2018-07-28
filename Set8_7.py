import math
x=int(input())
for i in range(1,math.ceil(x/2)+1):
	if(x%i==0):
		print(i,end=" ")
		
		
