x=input()
odd=""
even=""
for i in range(len(x)):
	if(i%2==0):
		odd+=x[i]
	else:
		even+=x[i]
print(odd,even)
 
