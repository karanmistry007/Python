list=[1,2,2,3,3,3,4]
print("List With Duplicate Values: ",list)

for a in list:
    if list.count(a)>1:
        list.remove(a)

print("List Without Duplcate Values: ",list)
