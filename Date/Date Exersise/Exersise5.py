# Find the day of the week of a given date
# Given:

# given_date = datetime(2020, 7, 26)


from datetime import datetime

given_date = datetime(2020,7,26)

# Method 1
print(given_date.strftime('%A'))

# Method 2
print(given_date.today().weekday())