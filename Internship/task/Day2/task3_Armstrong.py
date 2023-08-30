num=1634
sum=0
no=num
temp=num
count =0

while no!=0:
    count+=1
    no = no //10



while temp>0:
    digit=temp%10
    sum+=digit**count
    temp=temp//10

if sum==num:
    print(num," Is Armstrong Number")
else:
    print(num," Is not Armstrong Number")