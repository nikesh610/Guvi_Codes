x=input()
cnt=0
for i in range(len(x)):
	if(x[i].isdigit()):
		cnt=cnt+1
print(cnt)
