# Perfect Square

def PerfectSquare(x) :
    i = 1
    while(i**2 <= x):
        if ((x%i == 0) and (x/i == i)):
            return True
        i += 1
    return False

print(PerfectSquare(24))
