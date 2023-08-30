name=input("Enter The Name: ")

if str(name)==str(name[::-1]):
    print(name," Is Palindrome")
else:
    print(name," Is Not Palindrome")