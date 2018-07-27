n=int(input())
x=list(map(int,input().strip().split()))
x=sorted(x)
for i in range(len(x)):
	print(x[i],end=" ")
