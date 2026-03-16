#0 1 1 2 3 5 8 13
t=int(input())
print("enter the first number")
a=int(input())
print("enter the second number")
b=int(input())
print(a,b,end="\t")
while term>2:
	c=a+b
	print(c,end="\t")
	a=b
	b=c
	term=term-1
			