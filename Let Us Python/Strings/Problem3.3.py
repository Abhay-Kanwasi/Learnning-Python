# For the following string find out which are having only alphabets, which are numeric, which are alphanumeric, which are lowercase, which are uppercase. Also find out whether 'And Quiet flows the Don't begins with 'And' or ends with 'And':

# 'NitiAayog'
# 'And Quiet Flows The Don'
# '1234567890'
# 'Make $1000 a day

import time
s1 = 'NitiAayog'
s2 = 'And Quiet Flows The Don'
s3 = '1234567890'
s4 = 'Make $1000 a day'
print("\nSentences\n")
time.sleep(2)
print('Sentence1 =', s1)
print('Sentence2 =', s2)
print('Sentence3 =', s3)
print('Sentence4 =', s4)
time.sleep(2)

print("Operations can be performed : \n1.Check Only Alphabets\n2.Check Only Numeric\n3.Check Alphanumeric\n4.Check Lowecase\n5.Check Uppercase\n6.Startswith and Endswith\n")

time.sleep(2)
operation = int(input("Choose the operation : "))
time.sleep(2)

if operation == 1:
    print("Checking for alphabets..")
    time.sleep(2)
    print(f"Is Alphabetic Sentence 1 : {s1.isalpha()}")
    print(f"Is Alphabetic Sentence 2 : {s2.isalpha()}")
    print(f"Is Alphabetic Sentence 3 : {s3.isalpha()}")
    print(f"Is Alphabetic Sentence 4 : {s4.isalpha()}")

elif operation == 2:
    print("Checking for numeric..")
    time.sleep(2)
    print(f"Is Numeric Sentence 1 : {s1.isnumeric()}")
    print(f"Is Numeric Sentence 2 : {s2.isnumeric()}")
    print(f"Is Numeric Sentence 3 : {s3.isnumeric()}")
    print(f"Is Numeric Sentence 4 : {s4.isnumeric()}")

elif operation == 3:
    print("Checking for alphanumeric..")
    time.sleep(2)
    print(f"Is Alphanumeric Sentence 1 : {s1.isalnum()}")
    print(f"Is Alphanumeric Sentence 2 : {s2.isalnum()}")
    print(f"Is Alphanumeric Sentence 3 : {s3.isalnum()}")
    print(f"Is Alphanumeric Sentence 4 : {s4.isalnum()}")

elif operation == 4:
    print("Checking for lowercase..")
    time.sleep(2)
    print(f"Is Lowercase Sentence 1 : {s1.islower()}")
    print(f"Is Lowercase Sentence 2 : {s2.islower()}")
    print(f"Is Lowercase Sentence 3 : {s3.islower()}")
    print(f"Is Lowercase Sentence 4 : {s4.islower()}")

elif operation == 5:
    print("Checking for uppercase..")
    time.sleep(2)
    print(f"Is Uppercase Sentence 1 : {s1.isupper()}")
    print(f"Is Uppercase Sentence 2 : {s2.isupper()}")
    print(f"Is Uppercase Sentence 3 : {s3.isupper()}")
    print(f"Is Uppercase Sentence 4 : {s4.isupper()}")

elif operation == 6:
    print("Checking for startswith..")
    time.sleep(2)
    print(f"Startswith Sentence 1 : {s1.startswith('And')}")
    print(f"Startswith Sentence 2 : {s2.startswith('And')}")
    print(f"Startswith Sentence 3 : {s3.startswith('And')}")
    print(f"Startswith Sentence 4 : {s4.startswith('And')}")
    print("\nChecking for endswith..")
    time.sleep(2)
    print(f"Endsswith Sentence 1 : {s1.endswith('And')}")
    print(f"Endsswith Sentence 2 : {s2.endswith('And')}")
    print(f"Endsswith Sentence 3 : {s3.endswith('And')}")
    print(f"Endsswith Sentence 4 : {s4.endswith('And')}")

else:
    print("Please enter the valid number.\nHint : Number will be between 1 to 6")