# Prime number or not 

num = int(input("Enter a number : "))
if num == 1:
    print("This is a prime number.")
if num > 1:
    for i in range(2,num):
        if num%i==0:
            print("It is not a prime number.")
        else:
            print("It is a prime number")
        break
