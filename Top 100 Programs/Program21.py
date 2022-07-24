# Check wheather a character is alphabet or not.

ch = input("Enter a character  : ")
# Python takes 'a' as 97 and takes 'b' as 122 similarly 'A' as 65 and takes 'Z' as 90. 
if (ch>="a" and ch<="z") or (ch>="A" and ch<="Z"): 
    print("It is an alphabet.")
else:
    print("It is not a alphabet.")