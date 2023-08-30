a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=int(input("Enter Third Number: "))


if a==b & b==c:
    print("all are same")
    
elif a>=b & a>=c:
    print(a," is Bigger")

elif b>=a & b>=c:
    print(b," is Bigger")

else:
    print(c," is Bigger") 

    