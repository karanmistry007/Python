#Write a Python program to find the maximum and minimum values in a set.
set1={1,4,5,6,3,2}
print(set1)

print("Maximum Number: ",max(set1))
print("Minimum Number: ",min(set1))

print("Minimum Number: ",set1.pop())
set2=sorted(set1,reverse=True)
print("Maximum Number: ",set2.pop(0))
