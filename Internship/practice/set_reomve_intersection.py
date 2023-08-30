#Write a Python program to remove the intersection of a second set with a first set.
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

set3=set2.difference(set1)
print(set3)