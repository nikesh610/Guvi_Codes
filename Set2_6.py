import math

x,y=map(int,input().strip().split())
for i in range(x+1,y):
	cnt=0
	for j in range(1,math.ceil(i/2)+1):
		if(i%j==0):
			cnt+=1
	if(cnt==1):
		print(i,end=" ")
