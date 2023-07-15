# Program to calculate number of days between two dates.

from datetime import date

first_date = date(2022,4,21)
last_date = date(2023,3,22)

days_between = last_date - first_date

print(f'Difference between {first_date} and {last_date} is {days_between.days}.')