num=int(input("Enter The Number: "))
no=num
count=0
sum=0
mul=1
temp=num

while no!=0:
    count+=1
    no=no//10


while temp>0:
    digit=temp%10
    sum+=digit
    mul*=digit
    temp=temp//10

if mul==sum:
    print(num," Is Twin Number")
else:
    print(num," Is not Twin Number")
    