# Add a week (7 days) and 12 hours to a given date
# Given:

# # 2020-03-22 10:00:00
# given_date = datetime(2020, 3, 22, 10, 0, 0)

from datetime import datetime, timedelta

given_date = datetime(2020, 3, 22, 10, 0, 0)
print("Given date :",given_date)

days_to_add = 7

res_date = given_date - (timedelta(days=days_to_add,hours=12))

print("After adding 1 week and 1 hours in the given date :",res_date)
