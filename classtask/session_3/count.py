# inp = input("Input Word: ")
# inp2 = input
# counter = 0

# for len in inp:
#         print(len)

# inp = int(input("Input: "))

# for num in range(inp):
#     if num % 2 == 0:
#         print(num)


# for loop

# while <contidion>: num1 > num2

# inp = int(input("Input: "))

# num = 1000

# while num < inp:
#     print(num)
#     num += 1

# if i in range in range(1, 10):
#     if i == 5:
#         break
#     else:
#         print(i)

# for num in range(4):
#     for in range(1, 10):
#         if i == 5:
#             break
#         else:
#             print(i)
#             print("----")

# for i in range(1, 10):
#         if i == 5:
#             continue
#         else:
#             print(i)

# input1: until number to print
# input2: where need to break


range_num = int(input("Range: "))
break_point = int(input("Break: "))

if range_num < break_point:
    print("Out of range")
else:
    num = 0
    while num < range_num:
        if break_point == num:
            break
    print(num)
    num += 1
    

