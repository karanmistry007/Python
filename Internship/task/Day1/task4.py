year=int(input("Enter The Year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print ("The given year is a leap year")
        else:
            print ("It is not a leap year")
    else:
        print ("The given year is a leap year")
else:     
    print ("It is not a leap year")