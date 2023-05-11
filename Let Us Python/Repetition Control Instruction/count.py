String = 'Nagpur-440010'
count_alphabets = 0
count_numbers = 0
for i in range(len(String)):
    if String[i].isalpha() == True:
        count_alphabets += 1
    elif String[i].isdigit() == True:
        count_numbers += 1
    else:
        continue
print(f"The number of alphabets is {count_alphabets}.")
print(f"The number of numbers is {count_numbers}.")