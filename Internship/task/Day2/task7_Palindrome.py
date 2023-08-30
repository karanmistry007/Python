n = int(input("Enter a value:"))  
temp = n  
rev = 0  
while(n> 0):  
    digit = n% 10  
    rev = rev * 10 + digit
    n = n // 10  
if(temp == rev):  
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!")