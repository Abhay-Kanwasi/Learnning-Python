# A date is not a python build-in type so we import it from modulename datetime.

# Example : Print the current date

import datetime

x = datetime.datetime.now()

print(x)



#The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

#Example 2 : Display the name of the month:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

# You can also vice-versa use strptime() for it




# Example 3 : Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Here %A is a legal format code..

# Legal format codes in Date Module
# We can use it 


"""
Directive	    Description	                            Example	
%a	        Weekday, short version	                    Wed	
%A	        Weekday, full version	                    Wednesday	
%w	        Weekday as a number 0-6, 0 is Sunday	    3	
%d	        Day of month 01-31	                        31	
%b	        Month name, short version	                Dec	
%B	        Month name, full version	                December	
%m	        Month as a number 01-12	                    12	
%y	        Year, short version, without century	    18	
%Y	        Year, full version	                        2018	
%H	        Hour 00-23	                                17	
%I	        Hour 00-12	                                05	
%p	        AM/PM	                                    PM	
%M	        Minute 00-59	                            41	
%S	        Second 00-59	                            08	
%f	        Microsecond 000000-999999	                548513	
%z	        UTC offset	                                +0100	
%Z	        Timezone	                                CST	
%j	        Day number of year 001-366	                365	
%U	        Week number of year, Sunday as the first day of week, 00-53	52	
%W	        Week number of year, Monday as the first day of week, 00-53	52	
%c	        Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	        Century	                                    20	
%x	        Local version of date	                    12/31/18	
%X	        Local version of time	                    17:41:00	
%%	        A % character	                            %	
%G	        ISO 8601 year	                            2018	
%u	        ISO 8601 weekday (1-7)	                    1	
%V	        ISO 8601 weeknumber (01-53)	                01
"""



# timedelta() attribute of datetime:-

# Represent the difference between two datetime objects.

# Supported operators:

# add, subtract timedelta
# unary plus, minus, abs
# compare to timedelta
# multiply, divide by int
# In addition, datetime supports subtraction of two datetime objects returning a timedelta, and addition or subtraction of a datetime and a timedelta giving a datetime.