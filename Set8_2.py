vow=['a','e','i','o','u']
x=input()
x=list(set(x))
s=0
for i in range(len(x)):
	if(vow.count(x[i])==1):
		s=1
		break
	else:
		pass
if(s==1):
	print("yes")
else:
	print("no")
	
