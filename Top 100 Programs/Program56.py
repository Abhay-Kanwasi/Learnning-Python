# Print N number using for and while loop


n = int(input("Enter the value of n :"))

print("Using for loop : ")
for number in range(1,n):
    print(number, end=" ")

print("\n\nUsing while loop")
number = 1
while number < n+1:
    print(number, end=" ")
    number += 1 