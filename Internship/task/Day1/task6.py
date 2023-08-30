month=int(input("Enter The Monthly Salary: "))
salary=month*12
if salary>200000:
    net=salary-(salary*0.05)
    print("Net salary is ",net/12)

elif salary>500000:
    net=salary-(salary*0.1)
    print("Net salary is ",net/12)

elif salary>1000000:
    net=salary-(salary*0.15)
    print("Net salary is ",net/12)

elif salary>1500000:
    net=salary-(salary*0.2)
    print("Net salary is ",net/12)    

else:
    print("Net salary is ",salary/12)
