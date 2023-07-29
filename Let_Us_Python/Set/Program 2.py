# Set Operations

# Create a set

set = {12,15,12,16,19}

print(f'Set is unordered and don\'t allow duplicate values that\'s why old set become like this : {set}')

# in, not in 

set = {1,3,2,4,5,11}
if 1 in set:
    print(True)
if 2 not in set:
    print(False)
else:
    print('condition not matched nor \'in\' or nor for \'not in \'.')

# maximum and minimum value of a set.

set = {12,13,21,1,2,4}
print(f'Maximum value in {set} is {max(set)}.')
print(f'Minimum value in {set} is {min(set)}.')


# sorted set and sum of set

set = {1,2,3,11,0,3,2,23}
print(f'Sorted set : {sorted(set)}')

set = {1,2,3}
print(f"Sum of set : {sum(set)}")