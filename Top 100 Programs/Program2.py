# Smallest among three numbers.

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))

if a<b and a<c:
    print(a,"is the smallest number.")
if b<a and b<c:
    print(b,"is the smallest number.")
if c<a and c<b:
    print(c,"is the smallest number.")