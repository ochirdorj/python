# Task 1: Number info
# Description:
#  Ask the user to enter a number. Your program should:
# Check if the number is positive, negative, or zero
# Check if the number is even or odd
# Print both results
# Example:
# Input: -11  
# Output:
# The number is negative  
# # The number is odd

number = int(input("Please provide me the number you want to check:" ))

if (number % 2 == 0):
    print("Number is Even")
else:
    print("Number is Odd")
if (number > 0):
    print ("Number is Positive")
elif (number < 0):
    print("Number is Negative")
else:
    print("Number is Zero")


 
    