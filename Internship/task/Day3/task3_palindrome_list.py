list1 = ["anuj","karan","naman","mam","malayalam"]
list2 = []
for name in list1:
    if str(name) == str(name)[::-1]:
        list2.append(name)
print ("Palindrome Name From List are: ",list2)