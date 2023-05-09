# Valid triangle : Sum of all three angles is 180.

angle1 = input("Enter the value of angle 1 : ")
angle2 = input("Enter the value of angle 2 : ")
angle3 = input("Enter the value of angle 3 : ")

if angle1.isalpha() == True or angle2.isalpha() == True or angle3.isalpha()== True:
    print("Input Error : Please check your inputs. (Hint : Angles must be an integer.)")
else:
    angle1 = int(angle1)
    angle2 = int(angle2)
    angle3 = int(angle3)
    if angle1+angle2+angle3==180:
        print("This is a valid triangle.")
    elif angle1 > 180 or angle2>180 or angle3>180:
        print("Input Error : Please check your inputs. (Hint : Angle must smaller than 180.)")
    else:
        print("This is not a valid triangle.")
