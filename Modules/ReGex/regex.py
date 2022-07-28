# Regex : Regular Expression Regular Expression, is a sequence of characters that forms a search pattern.

#RegEx can be used to check "if a string contains the specified search pattern"(Important).

# Regex is not also not available with python we have to import it. We can import it by saying import re.

# Example : Search the string to see if it starts with "The" and ends with "Spain":

import re

txt = r"The rain in Spain"
x = re.search("^The.*Spain$",txt)

if x:
    print("Yes, This is a match.")
else:
    print("No, This is not a match.")


"""
We have diffrent functions under Regex.

1. findall : Returns a list containing all matches
2. search :	 Returns a Match object if there is a match anywhere in the string
3. split :   Returns a list where the string has been split at each match
4. sub :	 Replaces one or many matches with a string

"""

# Let's discuss about finditer function..

# Rule :- We use raw string in the regular expression.


