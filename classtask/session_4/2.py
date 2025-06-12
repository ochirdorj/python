# nested_loops

# for i in range(1, 11):
#     print(f"Run {i}")

#     for j in range(1, 6):
#         if j  == range()
#         print(j, end =' ')

#         print()
#         print('-----------')

# mutable and immutable data types

# it's change it's contents

# It can change
# List --> append(), pop(), change the order of the list, reverse the list, sort, ... without reassigning values

# lst = [1,2,3,4] 

# immutable data types are datatypes cannot be changed. These are:
# - String;
# = Integer;

# lst = ["Hello", "World", "test"]

# lst[2] = "Akumo"

# print(lst)

# # contatination 

# Tuple is read only not changeable.

tpl = (1, 2, 3, 4)
print(tpl[0:2])


tpl = (1, 2, 3, 4)
print(tpl[0:-1])

# tpl works only with comma. 

tpl = (1, 2, 3, 4)
print(tpl[::-1])

# it can contain list, Integer, float, boolean

# we can't put list in ahead of anything tuple
# only work with read only functions
# index() does not change tuple but it gives where value is located. 
#

lst = list(tpl) 

for num in tpl:
    print(num)