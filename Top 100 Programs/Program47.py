# Find prime factors

num = int(input("Enter the number : "))

for i in range(2, num+1):
    while num%i == 0:
        print(i, end=' ')
        num = num / i

