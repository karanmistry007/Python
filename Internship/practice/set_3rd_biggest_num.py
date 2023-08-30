set1=set()
num=int(input("Enter The Number of Values: "))
for i in range(0,num):
    val=int(input("Enter The Value:"))
    set1.add(val)



print("You Entered :",set1)
set2=sorted(set1,reverse=True)
x=set2.pop(2)
print("Third Biggest Number is: ",x)