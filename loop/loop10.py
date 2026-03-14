print("enter a number")
no=int(input())
for i in range(1,4,1):
	for j in range(1,11,1):
		if i==1:
			print(no*j,end="\t")
		elif i==2:
			print(j,end="\t")
		else:
			print(no,end="\t")
	print()