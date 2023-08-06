# Remove the second occurence of the number while not delting it's first occurence

def delete_second_occurence(list,number):
    found_count = 0
    index = 0
    while index<len(list):
        if list[index] == number:
            found_count += 1
            if found_count == 2:
                list.pop(index)
                break
        index+=1

numbers_list = [1,2,3,1,3,4]
print(f'Numbers before deleting second occurence : {numbers_list}')
number = int(input("Enter the number you want to delete second occurence of : "))

delete_second_occurence(numbers_list,number)

print(f'Number list after deleting second occurence of {number} is {numbers_list}')