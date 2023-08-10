# Like regular dictionary but remember the order item register 

# Because in older version of python (before python 3.7) dictionary was unordered.

from collections import OrderedDict
ordered_dict = OrderedDict()    
ordered_dict["b"] = 2
ordered_dict["a"] = 12
ordered_dict["d"] = 21
ordered_dict["c"] = 32
print(ordered_dict)
