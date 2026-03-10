print("basic salary")
salary=float(input())
da,hra=0,0
if salary>=5000:
	da=salary*0.3
	hra=salary*0.2
totalsalary=salary+da+hra
print("basic salary=",salary)
print("da=",da)
print("hra=",hra)
print("total salary=",totalsalary)