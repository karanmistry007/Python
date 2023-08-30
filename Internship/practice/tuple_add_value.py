tuple1=(1,2,3,4,5)
print("Tuple Without MOdification:",tuple1)
list=list(tuple1)
n=int(input("Enter The Number of Values: "))

for i in range(0,n):
    val=int(input("Enter The Value:"))
    list.append(val)

tuple1=tuple(list)
print("Updated Tuple:",tuple1)