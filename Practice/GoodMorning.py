import time
t=time.strftime('%H:%M:%S')
h=int(time.strftime('%H'))
print("Current Time Is:",t)
if 5<=h<11:
    print("Good Morning")
elif 11<=h<15:
    print("Good Afternoon")
elif 15<=h<20:
    print("Good Evening")
else:
    print("Good Night")