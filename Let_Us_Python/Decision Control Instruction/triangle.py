# Whether triangle is isosceles, equilateral, scalene or right triangle.

class Triangle_Properties:
    def triangle_is_isosceles(side1,side2,side3):
        if side1 == side2 or side2 == side3 or side3 == side1:
            return True
        else:
            return False

    def triangle_is_equilateral(side1,side2,side3):
        if side1 == side2 == side3:
            return True
        else:
            return False
        
    def triangle_is_scalene(side1,side2,side3):
        if side1 != side2 != side3:
            return True
        else: 
            return False
    
    def valid_triangle_by_angles(angle1,angle2,angle3):
            if angle1+angle2+angle3==180:
                return True
            else:
                return False
    
    def valid_triangle_by_sides(side1,side2,side3):
        if side1+side2>=side3 and side3+side1>=side2 and side2+side3>=side1:
            return True
        else:
            return False



    
