print("enter a number")
n=int(input())
last=n%10
while n!=0:
	r=n%10
	n=n//10
print("sum of first and last digit=",r+last)