num=int(input("Enter The Number: "))
rev=0
temp=num

while temp!=0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10

if rev==num:
    print(num," Is Palindrome Number")
else:
    print(num," Is Not Palindrome Number")