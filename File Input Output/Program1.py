# Write a program to read the contents of file 'messages' one character at a time. Print each character that is read.

with open('messages.txt', mode='a') as my_file:
    text = "I'm a computer science student"
    my_file.write(text + '\n')

# Reopen the file in read mode and read its contents
with open('messages.txt', mode='r') as my_file:
    print(my_file.readlines())

