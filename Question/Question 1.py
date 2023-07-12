# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def diffrentiator(sequence):
    if len(sequence) == len(set(sequence)):
        return True
    else:
        return False

numbers = [12,23,24,25,1,121]
print(diffrentiator(numbers))



# Problem : How can we do it using loops?

