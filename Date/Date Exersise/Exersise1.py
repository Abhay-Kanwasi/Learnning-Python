# Print current date and time in Python

import datetime

# This will print both date and time
x = datetime.datetime.now()
print("Current Date and Time :",x)


# This will print only time
y = datetime.datetime.now().time()
print("Only time is :",y)