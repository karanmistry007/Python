def findArmstrong(no):
    rem=0
    sum=0
    temp=no
    num=no
    count=0
    while no!=0:
        count+=1
        no=no//10

    while num!=0:
        rem=num%10
        sum+=rem**count
        num=num//10

    if temp==sum:
        return True
    else:
        return False
    
no = int(input("Enter a number: "))
if findArmstrong(no)==True:
    print("Armstrong")
else:
    print("Not Armstrong")    
        