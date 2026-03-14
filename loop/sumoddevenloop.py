print("enter a number")
n=int(input())
es,os,oc,ec=0,0,0,0
while n!=0:
	r=n%10
	if r%2==0:
		es=es+1
		ec=ec+1
	else:
		os=os+1
		oc=oc+1
	n=n//10
print("no of odd digits=",oc)
print("no of even digits=",ec)
print("sum of even digits=",es)
print("sum of odd digits=",os)