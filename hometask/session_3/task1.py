# Task 1: Reverse a List
# Write a program that reverses a list using a for loop.
# Example:

# Input:
# Enter numbers separated by space: 1 2 3 4 5
# Output:
# Reversed List: [5, 4, 3, 2, 1]

x = input("Enter numbers separated by spaces: ")

y = x.split()

z = []

for value in y:
    z = [value] + z
    print(z)

