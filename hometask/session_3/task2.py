# Task 2: Remove Duplicates from a List
# Ask the user to enter multiple words separated by spaces. Store them in a list and remove duplicate words while maintaining the original order.

# Example:
# Enter words: apple banana apple cherry banana apple  
# Filtered List: ['apple', 'banana', 'cherry']

words = input("Enter multiple words separated by spaces: ").split()

unique_words = []
seen = set()

for word in words:
    if word not in seen:
        unique_words.append(word)
        seen.add(word)

print("Words without duplicates:", unique_words)

