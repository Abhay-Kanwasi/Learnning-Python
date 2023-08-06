# Find the maximum and minimum value from a list with and without using perdefined function.

def using_min_max():
    limit = int(input("How many numbers you want to enter : "))
    numbers = []
    for number in range(1,limit+1):
        number = int(input(f"Enter the {number} number : "))
        numbers.append(number)

    print(f'Maximum number in the list : {max(numbers)}')
    print(f'Minimum number in the list : {min(numbers)}')

def without_using_min_max():
    
    pass


