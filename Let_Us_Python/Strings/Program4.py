# Write a program which will convert character into it's ASCII value and also vice-versa

chracter = ''
value = 0

choose = input("What do you want to enter ?\n1. Character\n2. Value\n")
if choose == '1':
    character = input("Enter the character : ")
    print(f'ASCII value of {character} is {ord(character)}.')
elif choose == '2':
    value = int(input("Enter the value : "))
    print(f'ASCII character of {value} is {chr(value)}.')
else:
    print("Choose either option 1 or option 2.")

