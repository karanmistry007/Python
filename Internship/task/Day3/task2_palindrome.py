a=["naman","anuj","kevin","naman"]

for b in a:
    if (str(b)==str(b)[::-1]):
        print("Palindrome Name: ",b)
        print("Count of Palindrome Name: ",a.count(b))
        