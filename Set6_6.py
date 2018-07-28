x=input()
a=0
n=0
for i in range(len(x)):
	if(a==0 and x[i].isalpha()):
		a+=1
		if(n>0 and a>0):
			break
	elif(n==0 and x[i].isdigit()):
		n+=1
		if(n>0 and a>0):
			break
	else:
		pass
if(a>0 and n>0):
	print("yes")
else:
	print("no")
	
	
