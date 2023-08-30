n = int(input("Enter the number: "))
r = 0
while(n!=0):
    digit = n%10
    r = r*10 + digit
    n //= 10

print("Reversed number: "+str(r))