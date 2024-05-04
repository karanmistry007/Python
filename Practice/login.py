user = {"karan": "1234", "vinay": "5678"}
x = 10


while x != 0:

    print(
        "1. Login \n2. Create Account \n3. Show Users \n4. Delete Account \n5. Update Details \n6. Exit"
    )
    inp = int(input("Choose an Option: "))

    match inp:
        case 1:
            print("Login")
            username = input("Enter the username: ")
            password = input("Enter the password: ")

            for i in user:
                if username == i:
                    if password == user[username]:
                        uname = username
                        print("Welcome ", uname, end="\n\n")
                    else:
                        print("Incorrect Password", end="\n\n")

            if username not in user:
                print("Incorret Username", end="\n\n")

        case 2:
            print("Create Account")
            username = input("Enter the username: ")
            password = input("Enter the password: ")

            user[username] = password
            print("User Created", end="\n\n")

        case 3:
            print("All Users")

            for i in user:
                print(i, " : ", user[i])

            print(end="\n\n")
        case 4:
            print("Delete Account")
            print("Login")
            username = input("Enter the username: ")
            password = input("Enter the password: ")

            for i in user:
                if username == i and password == user[i]:
                    deluser = username
            user.pop(deluser)
            print("User Has Been Deleted", end="\n\n")

        case 5:
            print("Update Details")
            print("Login")
            username = input("Enter the username: ")
            password = input("Enter the password: ")

            for i in user:
                if username == i and password == user[i]:
                    deluser = username
            print("Old Details: ", username, password)
            user.pop(deluser)
            usernamenew = input("Enter the username: ")
            passwordnew = input("Enter the password: ")
            user[usernamenew] = passwordnew
            print("User Has Updated", end="\n\n")

        case 6:
            print("Exit", end="\n\n")
            x = 0
