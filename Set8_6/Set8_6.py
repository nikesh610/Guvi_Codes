import math
x=int(input())
cnt=0
for i in range(1,math.ceil(x/2)+1):
	if(x%i==0):
		cnt+=1
if(cnt!=1):
	print("yes")
else:
	print("no")
