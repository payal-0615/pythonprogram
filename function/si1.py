def si():
	p=float(input("enter principal amaount"))
	r=float(input("enter rate of interest"))
	t=float(input("enter time"))
	si=p*r*t/100
	return si
res=si()
print("simple interest=",res)