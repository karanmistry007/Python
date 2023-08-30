list1 = [(1,2,3), (4,5,3), (2,3,4)]

# print(list1[0][0])

for _ in list1:
    for k in _:
        print(k,end=' ')  # (1,2,3)

# Dictioary -------------

print()
list1 = []
print(type(list1))

tup1 = ()
print(type(tup1))

dict1 = {}  
print(type(dict1))

set1 = set()

print(type(set1))

set2 = {23, 90.89, "String", 9+8j, False}
print(set2)

dict2 = {"Name" : "Aarav", 'roll' : 34, 'MArks' : 90.89, 80:78, "Name" : "Manoj"}
print(dict2)

# Dictionary -> Changeble, Don't allow Duplicates, Ordered ( In Python 3.6 and earlier, dictionaries are unordered.)
# Keys -> Unique

print(dict2)
print(type(dict2))  # <class 'dict'>

set1= {10,}
print(type(set1))  # <class 'set'>

dict3 = dict2.copy()
print(dict3)

dict4 = dict2

dict2.update({'school' : "HBK", "Address" : "Ahm", 89:[2,3,4,55]})

print(dict3)  # {'Name': 'Manoj', 'roll': 34, 'MArks': 90.89, 80: 78}
print(dict4)  # {'Name': 'Manoj', 'roll': 34, 'MArks': 90.89, 80: 78, 'school': 'HBK'}
print(len(dict4))  # returns Length of dict4
# print(dict2[2])  # GIves Error

print(dict2.get("Name"))  # Manoj

print(dict2.items())  # dict_items([('Name', 'Manoj'), ('roll', 34), ('MArks', 90.89), (80, 78), ('school', 'HBK'), ('Address', 'Ahm'), (89, [2, 3, 4, 55])])

print(dict2.keys())  # dict_keys(['Name', 'roll', 'MArks', 80, 'school', 'Address', 89])
print(dict2.values())  # dict_values(['Manoj', 34, 90.89, 78, 'HBK', 'Ahm', [2, 3, 4, 55]])

print(dict2.pop("Name"))
print(dict2)  # {'roll': 34, 'MArks': 90.89, 80: 78, 'school': 'HBK', 'Address': 'Ahm', 89: [2, 3, 4, 55]}

print(dict2.popitem())
print(dict2)
print(dict2.popitem())
print(dict2)

# for i in dict2:
#     print(i)


# for i in dict2.keys():
#     print(i)

# for j in dict2.values():
#     print(j)

# for y,z in dict2.items():
#     print(y,z,sep='\t')
for key,value in dict2.items():
    print(key,value)

x = ('key1', 'key2', 'key3')
y = 0
dict1.fromkeys(x,y)
print(dict1)

car = {
  "brand": "Mahindra",
  "model": "Thar",
  "year": 2017
}

x = car.setdefault("model", "Alto")

print(x)

# Mississippi

#  {'M' : 1, 'i' : 4, 's' : 4, 'p' : 2}


list1 = [23, 45, 90]
print(tuple(list1))
print(type(list1))

x = 90.10
print(int(float(x)))  # Explicit Typecasting

import math
print(math.ceil(x))
print(math.floor(x))

v = True  # 1
f = 90

print(f+v)  # Implicit typecasting


# --------------------------
dict4 = {
    'list1' : [10, 90,45,67,34,89],
    'list2' : [44, 90, 45, 12,23,48],
    'list3' : [3,4,6,7,89,90]
}

# Find Unique values from this dict4


# ------------------------------------------------

# set -> Don't Allow Duplicates, Unordered, Unchangeble*

# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.


# Frozen Sets -> UnOrdered, Immutable, Constant, Unique

set1 = {78, "Manoj", 89.90, 78, 78}

print(set1)
print(type(set1))  # <class 'set'>

set1.add("78")
print(set1)

set2  = set1.copy()
print(set2)

set3 = set1
print(set3)

print(id(set3))
print(id(set1))
print(id(set2))

set1 = {10, 90, 30, 40, 50, 60, "Manoj"}
set2 = {11, 66, 40, 30, 70, 90}
# print(set1.difference(set2))  # {50, 10, 60}


# set1.difference_update(set2)
# print(set1)  # {50, 10, 60}

set1.discard(7)   # does nothing, because 7 is not in the set
# print(set1)  # {50, 90, 10, 60, 30}

# set1.remove(7) #  raises a KeyError, because 7  is not in the set
print(set1)


# print(set1.intersection(set2))  # {90, 30}
# print(set1)
# print(set1.pop())
# print(set1.pop())
# print(set1)
# 

set1 = {10, 90, 30, 40, 50, 60}
set2 = {11, 66, 40, 30, 70, 90}
print(set1.symmetric_difference(set2))  # {66, 50, 70, 10, 11, 60}

set2.symmetric_difference_update(set1)
print(set1)

print(set1.union(set2))

set1.update('100')
print(set1)

list1 = [10, 90, 80, 45, 78]
list2 = [90,89,78,67]

list1.append(list2)
print(list1)  # [10, 90, 80, 45, 78, [90, 89, 78, 67]]


# list1.extend(list2)
# print(list1)  # [10, 90, 80, 45, 78, 90, 89, 78, 67]


list5 = ["Krutarth"]
list1.extend(list5)
print(list1)

set1 ={10,20,30,40}
set2 = {50,90}

print(set2.isdisjoint(set1))  # True
print(set2.issubset(set1))    # False
print(set1.issuperset(set2))  # False



# Tasks :---------------------------------------

'''
1. Check if a Given Key Already Exists in Dictionary
D1 = {'first_name' : 'Manish', 'age' : 22, 'height' : 5.0 , 'job' : 'Developer', 'company': 'Google'}


2. Handle Missing Keys in Dictionary
-> Dictionary is a collection in python, where the data is stored in the form of a key-value pair, that is, it maps key to its value. Often, you will not know all the keys present in the dictionary and you might end up with a typing error which may lead to runtime error due to missing keys in the dictionary.

D1 = {'first_name' : 'Zafar', 'age' : 21, 'height' : 4.8 , 'job' : 'Engineer', 'company': 'Microsoft'}

3. Extract Unique Values in a Given Dictionary
-> In a dictionary, the keys have to be unique, whereas the values can be duplicated. So, given a dictionary as shown below, how can you print all the unique values it has?

D1 = {	'list1': [4, 7, 10, 20], 
      	'list2': [7, 16, 9, 10], 
     	'list3': [13, 10, 4, 8], 
     	'list4': [7, 20, 6, 11]
         }

Output = [4, 6, 7, 8, 9, 10, 11, 13, 16, 20]

4. Print the Sum of Key Value Pairs in a Given Dictionary
-> You need to create a list which has the sum of key-value pairs of a given dictionary. 

D1 = {2: 8, 5: 20, 3: 15}

HINT-> This can be done using a for loop and append() function. 

5. Replace Dictionary Values From Other Dictionary
-> Let’s say you are given two dictionaries. You need to write a python program that will replace the values in the first dictionary with the values from the second dictionary if the key is present in the second dictionary. 

# initializing D1 - first dictionary
D1 = {'first_name' : 'Rutvi', 'age' : 21, 'height' : 4.0 , 'job' : 'Software Engineer', 'company': 'Uber'}
 
# initializing D2 - - first dictionary
D2 = {'age' : 35, 'job' : 'senior data analyst'}

6. Update or Change the Keys in a Given Dictionary
-> try these 2 ways
i)  Using assignment operator
ii) Using pop() method

D1 = {'Niraj': 23, 'Ashok': 29, 'Pushpa': 33, 'Sures': 40}

7. Delete a List of Keys in a Given Dictionary 

8. Count the Frequency of List Items Using a Dictionary
-> You can solve this in many ways. Any ideas? Well, you can just use looping constructs or use the list() count method or you can start with an empty dictionary and use the dict.get() method. Probably many other ways!

D1 = {'Niraj': 23, 'Krutarth': 29, 'Pushpa': 33, 'Sures': 40}

9. Change the Value of a Key in Nested Dictionary
-> Given a nested dictionary, you need to write a program demonstrating how to change the value associated with a particular key of that dictionary. 

#change the value of a key in nested dictionary
#Initializing Dictionary
D1 = {'emp1': {'name' : 'Niraj', 'age' : 21, 'job' : 'developer'}, 
      'emp2': {'name' : 'Zafar', 'age' : 22, 'job' : 'web dev'}, 
      'emp3': {'name' : 'Rutvi', 'age' : 22, 'job' : 'developer'}, 
      'emp4': {'name' : 'Ashok', 'age' : 60, 'job' : 'python developer'}}

11. Check if the Given Dictionary Is Empty or Not
-> One way to check this using the len() function, which you can try coding; we will achieve this using the bool() function. The bool() function evaluates to standard true or false and is used to return or convert a value to Boolean type. If you pass an empty dictionary, the bool() evaluates to False, as failure to convert something that is empty.

14. Get a Key From Value in a Dictionary
-> You need to write a program, which returns the key for a given value. This can be done in multiple ways. Try doing it using dict.items() function.

#get key for a given value using dict.items()
# Dictionary Initialization
D1 = {'Priyanka Chopra': 23, 'Alia Bhatt': 29, 'Hritik Roshan': 45, 'Ranbir Kapoor': 40}

15. Sort a Given Dictionary by Key
-> You know this so, you got this...

D1 = {'Niraj': 23, 'Jaynam': 29, 'Rutvi': 40, 'Zafar': 45, 'Obama': 34}

# ---------------------------------------------------------------------------------------------------------
# 1. Python program to assign frequency to tuples

# Input:
# tupList = [(4, 1), (3, 3), (4, 1), (5, 7), (3, 3), (4, 1)]


# 2. Python program to sort tuples by total digits

# Unsorted Tuple list : [(43343, 1), (2, 4), (12, 40), (1, 23)]
# Sorted Tuple list : [(2, 4), (1, 23), (12, 40), (43343, 1)]

tupList = [(43343, 1), (2, 4), (12, 40), (1, 23)]

# ---------------------------------------------------------------------------------------------------------

1. Write a Python program to find the third largest number from a given list of numbers.Use the Python set data type.----------
2. Write a Python program to find all the anagrams in a given list of strings and then group them together. (use set)************
3. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value-----------
4. Write a Python program to find elements in a given set that are not in another set.---------------
5. Write a Python program to find the maximum and minimum values in a set.-----------------
6. Write a Python program to remove the intersection of a second set with a first set.--------------
'''