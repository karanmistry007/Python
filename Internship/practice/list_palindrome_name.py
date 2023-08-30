list=["naman","anuj","kevin","naman"]

for a in list:
    if str(a)==str(a[::-1]):
        print("Palindrome Name: ",a)
        print("Count of Palindrome Name:",list.count(a))
