for b in range(1,21,1):
	if b==0 or b==1:
		continue
	c=0
	for p in range(2,b//2+1,1):
		if b%p==0:
			c=c+1
	if c==0:
		print(b,"is prime number")
	else:
		print(b,"is not prime number")
	
