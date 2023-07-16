# Write a program to print the calender of a given month and year.

import calendar

year = int(input("Enter a year : "))
month = int(input("Enter a month : "))
print(calendar.month(year,month))