dict1 = {}
num=int(input("Enter The Number of Value:"))

for i in range (0,num):
    a=input("Enter Key:")
    b=input("Enter Value:")
    dict1.update({a: b})

print(dict1)