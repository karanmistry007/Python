list1 = [1, 5, 3, 7, 9,4,8]
sum = 12
ans = []
l=len(list1)
for i in range(0,l):
    num = list1.pop()
    diff = sum - num
    if diff in list1:
        ans.append((diff, num))
          
ans.reverse()
print(ans)
