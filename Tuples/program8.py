# from copy import deepcopy

# tuplex = ('hello', 5, [], True)
# print(tuplex)

# tuplex_clone = deepcopy(tuplex)
# tuplex[2].append(50)
# print(tuplex_clone)



hytrogenious_data = ('hello', 5, [], True)

clone_tuple = hytrogenious_data

clone_tuple[2].append(50)
print(clone_tuple)


"""
In the first code snippet, deepcopy creates a separate, deep copy of the original tuple, ensuring that changes to one do not affect the other.
In the second code snippet, a reference assignment is made, so both variables reference the same tuple object, and changes to one affect the other.
"""