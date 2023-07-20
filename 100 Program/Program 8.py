# Calcualte the simple intrest 

principal = int(input("Enter the principal amount : "))
rate = float(input("Enter the rate : "))
time = float(input("Enter the time : "))

simple_intrest = (principal*rate*time)/100

print(f'Simple Intrest : {simple_intrest}')