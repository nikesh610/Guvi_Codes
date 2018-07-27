x=input()
cnt=0
for i in range(len(x)):
	if(x[i].isdigit() or x[i]==" "):
		pass
	elif(x[i].isalpha() or x[i]==" "):
		pass
	else:
		cnt+=1
print(cnt)
