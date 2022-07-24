# Sum of n natural number using while loop

print("This is a program for sum of n natural number using while loop")
# n = 10
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)

n = int(input("Enter the value of n :"))
i = 0
sum = 0
while i<=n:
    sum += i
    i+=1
print(sum)
