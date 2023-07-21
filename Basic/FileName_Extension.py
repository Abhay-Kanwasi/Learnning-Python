# Program to accept a filename from the user and print the extension of that

filename = input("Enter the filename : ")
file_extension = filename.split('.')
print(f"File '{filename}' have file extension {file_extension}")