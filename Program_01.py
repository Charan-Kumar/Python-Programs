__author__ = 'charan'

#1. Write a program to find roots of quadratic equation

import math
def quadratic_equation(a,b,c):
    determinent = b*b-(4*a*c)
    if determinent > 0:
        r1 = (-b + math.sqrt(determinent))/(2*a)
        r2 = (-b - math.sqrt(determinent))/(2*a)
        print("The Roots are ",r1," ",r2)
    elif determinent == 0:
        r1 = r2 = -b/(2*a)
        print("The Roots ara ",r1," ",r2)
    else:
        print("The Roots are Imaginary")

quadratic_equation(2,5,4)