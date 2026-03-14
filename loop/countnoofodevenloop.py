print("enter a number")
n=int(input())
ec=0
oc=0
while n!=0:
	r=n%10
	if r%2==0:
		ec=ec+1
	else:
		oc=oc+1
	n=n//10
print("no of even digits=",ec)
print("no of even digits=",oc)