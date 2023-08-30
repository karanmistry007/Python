a=[1,2,3,5,5,5,4,8,8]
print("list with duplicate: ",a)
for element in a:
    if(a.count(element)>1):
        a.remove(element)
print("List wuthout duplicate: ",a)