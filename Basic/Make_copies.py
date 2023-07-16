# Make copy of given string 

string = input("Enter the string : ")
n = int(input("Enter how many time you want to print it : "))
result = ''
for i in range(n):
    result = result + string
print(result)