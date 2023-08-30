dict1={
    "list1" : [10,90,45,67,34,89],
    "list2" : [44,90,45,12,23,48],
    "list3" : [3,4,6,7,89,90]
}
#find the unique values
print("Dictionary is: ",dict1)

set1=set(dict1.pop("list1"))
set2=set(dict1.pop("list2"))
set3=set(dict1.pop("list3"))

unique=set1.difference(set2)
unique=unique.difference(set3)
print("Unique values are: ",unique)
