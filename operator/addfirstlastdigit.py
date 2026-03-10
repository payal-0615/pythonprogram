a=int(input("enter a four digit number"))
last_digit=a%10
first_digit=a//1000
sum=first_digit+last_digit
print("first digit=",first_digit)
print("last digit=",last_digit)
print("sum of first and last digit=",sum)