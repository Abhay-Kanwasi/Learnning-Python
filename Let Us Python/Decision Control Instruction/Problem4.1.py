# While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 1000. If quantity and price per item are input through the keyboard, write a program to calculate the total expenses.

quantity = int(input("Enter the value of quantity : "))
price = float(input("Enter the price of item : "))
if quantity > 1000:
    discount = 10
else: 
    discount = 0

total_expense = quantity * price - quantity * price * discount/100
print(f"The total expense is Rs. {total_expense}.")