# Task 3: Find the Longest Word in a List
# Ask the user to enter a list of words. Find and print the longest word from the list.

# Example:
# Enter words: Python Java JavaScript C  
# Longest word: JavaScript  

words = input("Enter all words: ").split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
        print(word)
    
