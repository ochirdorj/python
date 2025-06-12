x = 2
y = 4
z = 6



if x == y == z:
    print("Equilateral triangle")
elif x == y != z or x == z != y or y == z != x:
    print("Isosceles triangle")
elif x + y < z or x + z < y or y + z < x:
    print("Not a triangle")
elif x != y != z:
    print ("Scalene triangle")
else:
    print("Wrong input")




if  x + y < z:
    print("Good")
elif  x + z < y:
    print("Bad")
elif  y + z < x:
    print("option3")
else:
    print("Zub hariu")