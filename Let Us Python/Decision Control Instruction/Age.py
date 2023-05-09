Age_Ram = int(input("Enter the age of Ram : "))
Age_Shyam = int(input("Enter the age of Shyam : "))
Age_Ajay = int(input("Enter the age of Ajay : "))

if Age_Ram < Age_Ajay and Age_Ram < Age_Shyam:
    print(f"Ram is the youngest of the three.")

elif Age_Shyam < Age_Ajay and Age_Shyam < Age_Ram:
    print(f"Shyam is the youngest of the three.")

elif Age_Ajay < Age_Ram and Age_Ajay < Age_Shyam:
    print(f"Ajay is the youngest of the three.")

else:
    print("Please enter the correct age (Hint : Age must be a integer.)")