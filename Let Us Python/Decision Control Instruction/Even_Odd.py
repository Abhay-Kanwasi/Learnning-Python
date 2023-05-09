# Any integer is input through the keyboard. Write a program to find out whether it is an odd number or even number.

integer = int(input("Enter the nubmer :"))
if integer==0:
    print(f"{integer} is neither a odd number or even number.")
elif integer%2==0:
    print(f"{integer} is an even number.")
else:
    print(f"{integer} is an odd number.")