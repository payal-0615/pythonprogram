print("enter a number")
num=int(input())
if num<10:
    print("Single digit number")
elif num<100:
    print("Double digit number")
elif num<1000:
    print("Triple digit number")
else:
    print("Other number")