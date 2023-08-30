a=int(input("Enter the number: "))
n=a

strn=str(a)
sum=0

for digit in strn:
    sum += int(digit)


strn=str(n)
product=1

for digit in strn:
    product *= int(digit)

if(sum==product):
    print("Number is twin number")
else:
    print("Number is not twin number")