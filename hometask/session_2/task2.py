# Task 2: Final Decision
# Description:
#  Take two boolean inputs from the user (True or False) and show the result of and, or, and not operations.
# Example:
# Input:
# First Boolean: True  
# Second Boolean: False  
# Output:
# True and False = False  
# True or False = True  
# not True = False

first = input("Please provide me your first booelean: ")
second = input("Please provide me your second booelean: ")

if first == "true" and second == "true":
    print(f"{first} and {second} = {True and True}")

elif first == "false" and second == "true":
    print(f"{first} and {second} = {False and True}")

elif first == "true" and second == "false":
    print(f"{first} and {second} = {True and False}")

elif first == "false" and second == "false":
    print(f"{first} and {second} = {False and False}")

if first == "true" or second == "true":
    print(f"{first} or {second} = {True or True}")

elif first == "false" or second == "true":
    print(f"{first} or {second} = {False or True}")

elif first == "true" or second == "false":
    print(f"{first} or {second} = {False or True}")

elif first == "false" or second == "false":
    print(f"{first} or {second} = {False or False}")

if first == "true":
     print(f"Not False = {True}")

if first == "false":
     print(f"Not True = {False}")