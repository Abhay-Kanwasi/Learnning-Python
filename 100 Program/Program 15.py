# Convert bytes to KB,MB,GB,TB

bytes = int(input("Enter the number of bytes : "))

# KB = B * 1024
# MB = KB * 1024
# GB = MB * 1024
# TB = GB * 1024

operation = int(input("What operation you want to perform :\n1. Convert to KB\n2. Convert to MB\n3. Convert to GB\n4. Convert to TB\nYour choice : "))

if operation == 1:
    # Convert byte to kilobyte
    kb = bytes/1024
    print(f'{bytes} converted to {kb} kilobytes.')

elif operation == 2:
    # Convert byte to megabyte
    mb = bytes/(1024*1024)
    print(f'{bytes} converted to {mb} megabytes.')

elif operation == 3:
    # Convert byte to gigabyte
    gb = bytes/(1024*1024*1024)
    print(f'{bytes} converted to {gb} gigabytes.')

elif operation == 4:
    # Convert byte to terabyte
    tb = bytes/(1024*1024*1024*1024)
    print(f'{bytes} converted to {tb} terabytes.')

else:
    print("Please choose the valid operation.")
