# Solve Quadratice Equation

# -b +- (b**2 - 4ac)/2a

a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = float(input("Enter the value of c : "))

discriminant = (b**2 - (4*a*c))
if discriminant > 0:
    quadractic_equation1 = (-b + discriminant)/2*a
    quadractic_equation2 = (-b - discriminant)/2*a
    print(f'Solve : {quadractic_equation1},{quadractic_equation2}')
elif discriminant == 0:
    quadractic_equation1 = quadractic_equation2 = -b /(2 * a)
    print(f'Two equals and real roots are {quadractic_equation1}, {quadractic_equation2}')
elif discriminant < 0:
    quadractic_equation1 = quadractic_equation2 = -b / (2 * a)
    imaginary = (-discriminant)**0.5/(2 * a)
    print(f'Two distinct complex roots are {quadractic_equation1} : {imaginary : 2f}, {quadractic_equation2} : {imaginary : .2f}')
