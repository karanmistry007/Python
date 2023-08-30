def getData(no,*args):
    print(args)
    print("no--->",no)
    for i in args:
        print(i)

getData(70,"karan","kevin")

def getData1(*args):
    print(args)
    for i in args:
        print(i)

getData1(15,25,35)