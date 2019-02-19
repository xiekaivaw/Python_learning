import math
def quadratic(a, b, c):
    if not isinstance (a,(int,float)):
        raise TypeError('bad operand type')
    dat = b*b - 4*a*c
    x1 = ((-b+math.sqrt(dat))/2)/a
    x2 = ((-b-math.sqrt(dat))/2)/a
    return x1,x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('error')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('error')
else:
    print('success')