s=0
for b in range(1,21,1):
	if b==0 or b==1:
		continue
	c=0
	for p in range(2,b//2+1,1):
		if b%p==0:
			c=c+1
	if c==0:
			s=s+b
			print(b,"is prime number")
print("sum of prime numbers=",s)
	