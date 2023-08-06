# Check the given number is armstrong number or not.


# Limited scope


# number = 371

# str_number = str(number)

# if (int(str_number[0])**len(str_number)) + (int(str_number[1])**len(str_number)) + (int(str_number[2])**len(str_number)) == int(str_number):
#     print(f'{number} is an armstrong number.')
# else:
#     print(f'{number} is not an armstrong number.')



# Explicit Scope

number = input("Enter the number : ")

result = 0 # In result we will store the calculation of given number 

for element in range(len(number)):
    result += int(number[element])**len(number)
if result == int(str(number)):
        print(f'{number} is an armstrong number.')
else:
    print(f'{number} is not an armstrong number.')
    