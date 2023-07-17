import time
try:
    x1 = float(input("x1 : "))
    y1 = float(input("y1 : "))
    x2 = float(input("x2 : "))
    y2 = float(input("y2 : "))
    x3 = float(input("x3 : "))
    y3 = float(input("y3 : "))
    print("\nWhich method you want to use ?\n1. Area of triangle\n2. By finding the slope\n")
    time.sleep(2)
    method = int(input("Your choice : "))
    if method == 1 or method == 2:
        if method == 1:
            # Approch 1 : By finding the area of triangle
            print("Using method area of triangle..\n")
            time.sleep(2)
            y2minusy3 = y2 - y3
            y3minusy1 = y3 - y1
            y1minusy2 = y1 - y2
            area_of_triangle = 0.5 * (x1 * y2minusy3 + x2 * y3minusy1 + x3 * y1minusy2)
            if area_of_triangle == 0:
                print("Yes, All three points fall on one stright line.")
            else:
                print("No, All three points not fall on one straight line.")
        if method == 2:
            # By finding the slope
            print("Using method finding the slope..\n")
            time.sleep(2)
            m1 = (y2 - y1) / (x2 - x1)
            m2 = (y3 - y2) / (x3 - x2)
            if m1 == m2:
                print("Yes, All three points fall on one stright line.")
            else:
                print("No, All three points not fall on one straight line.")
    else:
        print("Input Error : Please enter the valid choice.\n(Hint : Input must be an integer.)")
except ValueError:
    print("Value Error : Points must be a integer.")

