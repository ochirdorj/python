year = int(input("Please provide your year to check leap year: "))


if year % 4 == 0 or year % 400 == 0:
    print("It's a leap year")
elif year % 4 == 0 or year % 100 == 0:
    print("It's not a leap year")
else:
    print("It's not a leap year")

