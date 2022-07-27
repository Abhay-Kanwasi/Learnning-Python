# Print date in a following format

# Given:
# given_date = datetime(2020, 2, 25)

# Expected output: 
# Tuesday 25 February 2020

from datetime import datetime

given_date = datetime(2020, 2, 25)

print(given_date.strftime('%A %d %B %Y'))