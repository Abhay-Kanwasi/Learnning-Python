# Get the ASCII value of char

character = input("Enter the single character(not words) : ")
ascii_value = ord(character)
print(f'Character : {character}\nASCII value : {ascii_value}')


# Get the Character of ASCII value

ascii_value = int(input("Enter the ASCII value : "))
character1 = chr(ascii_value)
print(f'ASCII Value : {ascii_value}\nCharacter : {character1}')