no=1
no1=0
for b in range(1,5,1):
	no1=no+b
	for p in range(1,b+1,1):
		if b%2==0:
			no1=no1-1
			print(no1,end="\t")
		else:
			print(no,end="\t")
		no=no+1
	print()
