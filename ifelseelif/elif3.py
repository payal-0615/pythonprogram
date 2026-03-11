print("enter a number")
no=int(input())
if no%35==0:
    print("Number is divisible by both 5 and 7")
elif no%5==0:
    print("Number is divisible by only 5")
elif no%7==0:
    print("Number is divisible by only 7")
else:
    print("Number is not divisible by 5 and 7")
