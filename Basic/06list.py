#!/usr/bin/python
# create a list in python
language = ["Java", "Python", "Golang", "PHP", "JavaScript", "C#"]
# accessing list elements
print(language[0][2])  # display: v
print(language[0][3])  # display: a
print(language[-2])    # display: JavaScript
print(language[1:3])   # display: ["Python", "Golang"]
print(language[3:])    # display: ["PHP", "JavaScript", "C#"]
print(language[:])     # display: ["Java", "Python", "Golang", "PHP", "JavaScript", "C#"]
# delete list elements
myList = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
print("items", len(myList))
print("deleting", myList[2], "....")
del myList[2]       # delete the item: o
print("done")
print("items", len(myList))