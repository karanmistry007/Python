data={"message":[{"name":"jay","score":"100"},{"name":"karan","score":"100"},{"name":"karan","score":"100"},{"name":"jay","score":"100"},{"name":"karan","score":"100"}]}
que=["karan","jay"]
ans=[]
temp=[]
dic2={}

lis=data["message"]
for name in que:
    for dic1 in lis:
        if dic1["name"]==name:
            print(name)
            temp.append(dic1)
    dic2[name]=temp
    temp=[]
print(dic2)