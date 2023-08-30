num=int(input("Enter The Number:"))
sum=0
count=0
temp=num
no=num

while no!=0:
    count+=1
    no=no//10

print("Number of character are: ",count)

while temp>0:
    digit=temp%10
    sum+=digit**count
    temp=temp//10

if sum==num:
    print(num," Is Armstrong Number")
else:
    print(num," Is not Armstrong Number")