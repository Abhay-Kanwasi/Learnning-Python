# Find wheather a year is a leap year or not.

year = int(input("Enter a year :"))
if year%4:
    if year%100:
        print("It is a leap year.")
    else:
        print("It is not a leap year.")
else:
    if year%400==0:
        print("It is a leap year.")
    else:
        print("It is not a leap year.")


# Approch 2

year = int(input("Enter a number :"))
if year%400 and year%4==0 and year%100:
    print("It is a leap year.")
else:
    print("It is not a leap year")


# Approch 3

year = int(input("Enter a year : "))
print("It is a leap year") if year%4==0 and year%100==0 and year%400==0 else print("It is not a leap year.")


