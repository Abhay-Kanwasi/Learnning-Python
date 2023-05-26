# my_file = open('test.txt')
# print(my_file.read())
# print(my_file.readline())
# print(my_file.seek(0))
# print(my_file.readlines())
# my_file.close()

# Standard way to read a file
# with open('test.txt',mode='a') as my_file:
#     text = my_file.write("\nI'm a computer science student.")
#     print(my_file.readlines())



# Created a new file if it doesn't exist.
with open('creation.txt',mode='w') as creation:
    text = creation.write("We are good people.")
    print(creation)

