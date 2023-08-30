n=int(input("Enter The Value of n: "))
count=1
sum=0
a=0
b=1

print("Fibonacci Series:",end=" ")

while count<=n:
    print(sum,end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b

