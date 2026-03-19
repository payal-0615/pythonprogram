n=int(input("enter a number"))
b=0
for a in range(2,n//2+1,1):
	if n%a==0:
		b=b+1
if b==0:
	print(n,"is prime number")
else:
	print(n,"is not prime number")