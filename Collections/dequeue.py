# Dequeue : It is an double ended queue. It can remove add or remove elements from both ends

from collections import deque

d = deque()

d.append(1) # ([1])
d.append(2) # ([1,2])
d.appendleft(3) # ([3,1,2])
# No need of right because it will already appending items to right
d.popleft() # ([1,2])
# No need of right because it will already poping items from right
list1 = [2,4,1,8] 
d.extend(list1) # ([1,2,2,4,1,8])

d.rotate(1)

print(d)
