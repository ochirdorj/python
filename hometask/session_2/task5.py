# Task 5: Triangle Type Checker
# Description:
#  Ask the user for 3 side lengths and determine what type of triangle they form:
# Equilateral: all sides equal
# Isosceles: two sides equal
# Scalene: all sides different
# Not a triangle: if the sum of any two sides is not greater than the third
# Example:
# Input: 5, 5, 5  
# Output: Equilateral triangle

x, y, z = input("Enter your 3 side triangle lenght: ").split()

print(x, y, z)

if x == y == z:
    print("Equilateral triangle")
elif x == y != z or x == z != y or y == z != x:
    print("Isosceles triangle")
elif x + y < z:
    print("Not a triangle")
elif x + z < y:
    print("Not a triangle")
elif y + z < x:
    print("Not a triangle")
elif  x != y != z:
    print ("Scalene triangle")
else:
    print("Wrong input")
