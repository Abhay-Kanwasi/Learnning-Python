# Add two binary string in Python using bin and int function.
# first decimal value 3
num1 = '00011'
# second decimal value 17
num2 = '10001'

# sum = first + second (17+3=20) sum = 20 (so now we calculate the decimal value of 20)
sum = bin(int(num1,2)+int(num2,2))  # Here we are using 2 because binary have base 2.
print(sum)



"""
base 2 of binary number means as we know we only have 2 binary numbers( 1 and 0 )

i.e. decimal number have base 10 which means (0,1,2,3,4,5,6,7,8,9) total 10 digits.

"""

