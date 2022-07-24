# Sum of all digit in a number.

# digit = input("Enter a number :")
# sum = 0
# for i in digit:
#     sum = int(i) + sum
# print(sum)


num = int(input("Enter a number :"))
result = 0
while num>0:
    rem = num%10
    result = result+rem
    num = int(num/10)
print("Result :",result)