#e gadgets login
a_username="admin"
a_password="admin"
c_username="customer"
c_password="customer"
a=0

def admin_login():
    print("Admin Login")
    admin_username=input("Enter User Name: ")
    admin_password=input("Enter The password: ")
    if admin_username==a_username and admin_password==a_password:
        print("Admin Login sucessful")
    else:
        print("Username or password is wrong")
    

def customer_login():
    print("Customer Login")
    customer_username=input("Enter User Name: ")
    customer_password=input("Enter The password: ")
    if customer_username==c_username and customer_password==c_password:
        print("Customer Login sucessful")
    else:
        print("Username or password is wrong")

while a<3:
    print("E gadgets")
    print("1------->admin login")
    print("2------->customer login")
    print("3------->exit")
    a=int(input("Enter your choice: "))

    if a==1:
        admin_login()
    elif a==2:
        customer_login()
    elif a==3:
        break