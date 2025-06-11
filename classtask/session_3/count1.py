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