a=int(input("enter a four digit number"))
first=a//1000
last=a%10
middle=(a%1000)//10
newnumber=last*1000+middle*10+first
print("number after reversing first and last digit=",newnumber)
