list1 = ["anuj","karan","naman","mam","malayalam"]
list2 = []

for a in list1:
    if str(a)==str(a[::-1]):
        list2.append(a)

print("List With Palindrome Name:",list2)