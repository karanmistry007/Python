#Write a Python program to find all the anagrams in a given list of strings and then group them together. (use set)
list1=["care","knee","race","keen","god","dog"]
dict1 = {}

for string in list1:

    sorted_string = str(sorted(string))

    if sorted_string in dict1:

      dict1[sorted_string].append(string)
    else:

         dict1[sorted_string] = [string]

print(list(dict1.values()))