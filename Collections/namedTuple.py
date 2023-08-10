# nametuple : easy to create and light weight object similar to struct

from collections import namedtuple 
Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt) # Output : Point(x=1, y=4)
print(pt.x, pt.y)   # Output : 1, -4

print(pt[0] + pt[1])