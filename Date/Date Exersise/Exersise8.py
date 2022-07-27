# Convert the following datetime into a string
# Given:

# given_date = datetime(2020, 2, 25)

from datetime import datetime


given_date = datetime(2020, 2, 25)

string_time = given_date.strftime('%Y-%m-%d %H:%M:%S')

print(string_time)