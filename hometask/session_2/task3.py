# Task 3: Password Validator
# Description:
#  Ask the user to input a password.
#  Check if it meets all of the following conditions:
# At least 8 characters long
# Contains the letter “@”
# Does not contain any spaces
# Print:
# "Strong password" if all conditions are met
# Otherwise, print "Weak password"
# Example:
# Input: hello@123  
# Output: Strong password

password = input("Provide me your password please: ")

x = (len(password))
y = " "

if "@" in password and x >= 8 and not(y in password):
    print("Strong password")
else:
    print("Weak password")