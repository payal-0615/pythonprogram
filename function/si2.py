def si():
	si=p*r*t/100
	return si
print("enter principal amount")
p=float(input())
print("enter rate of interest")
r=float(input())
print("enter time")
t=float(input())
res=si()
print("simple interest=",res)