# Task 4: Find the Second Largest Number in a List (No max() or sort())
# Ask the user to enter a list of numbers. Find and print the second largest number without using max() or sort().

# Example:
# Enter numbers: 10 45 78 23 89 56  
# Second largest number: 78

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num

if second_largest == float('-inf'):
    print("No second largest value found.")
else:
    print("Second largest number:", second_largest)
