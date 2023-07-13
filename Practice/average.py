# Take input from user that how many items he wants to average of and then take that numbers from user.

number_of_inputs = int(input("How many numbers average you want : "))

sum = 0
for i in range(number_of_inputs):
    number = int(input("Enter the number : "))
    sum += number

average = sum/number_of_inputs

print(f'Average is : {average}')

