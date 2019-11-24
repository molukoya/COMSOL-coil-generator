# This is a program that helps to calculate points on an angular coil, you will find a sample of the coil generated
# in the parent folder. This program takes the small radius, r; big radius, R; coil numbers, in_coil_no; thickness;
# spacing, space; and the angle.
from math import *

# Variables for the coil
r = 10
R = 20
in_coil_no = [0, 1, 2, 3, 4, 5, 6]
space = 0.3
thickness = 0.4
angle = 60
theta = angle/2

# Extra variables extrapolation from given variables
last_internal_point = in_coil_no[-1]+1
ex_coil_no = in_coil_no[::-1]
total_space = thickness+space
b = total_space/sin(radians(theta))
c = thickness/sin(radians(theta))

with open('angular-coil.txt', 'a') as f:

    # The internal turn
    for coils in in_coil_no:
        if coils == 0:
            y11 = (r-total_space)*cos(radians(theta))
            x11 = -(r-total_space)*sin(radians(theta))
        else:
            y11 = ((r-(coils * (b - total_space)))*cos(radians(theta))+(coils*b))
            x11 = -((r-(coils * (b - total_space)))*sin(radians(theta)))

        y21 = ((R-(coils * (total_space + b)))*cos(radians(theta)))+(coils*b)
        y22 = ((R-(coils * (total_space + b)))*cos(radians(theta/2)))+(coils*b)
        y23 = ((R-(coils * (total_space + b)))*cos(radians(theta*0)))+(coils*b)
        y24 = ((R-(coils * (total_space + b)))*cos(radians(theta/2)))+(coils*b)
        y25 = ((R-(coils * (total_space + b)))*cos(radians(theta)))+(coils*b)

        y15 = ((r-(coils * (b - total_space)))*cos(radians(theta)))+(coils*b)
        y14 = ((r-(coils * (b - total_space)))*cos(radians(theta/2)))+(coils*b)
        y13 = ((r-(coils * (b - total_space)))*cos(radians(theta*0)))+(coils*b)
        y12 = ((r-(coils * (b - total_space)))*cos(radians(theta/2)))+(coils*b)

        x21 = -((R - (coils * (total_space + b))) * sin(radians(theta)))
        x22 = -((R - (coils * (total_space + b))) * sin(radians(theta/2)))
        x23 = ((R - (coils * (total_space + b))) * sin(radians(theta*0)))
        x24 = ((R - (coils * (total_space + b))) * sin(radians(theta/2)))
        x25 = ((R - (coils * (total_space + b))) * sin(radians(theta)))

        x15 = ((r-(coils * (b - total_space))) * sin(radians(theta)))
        x14 = ((r-(coils * (b - total_space))) * sin(radians(theta/2)))
        x13 = ((r-(coils * (b - total_space))) * sin(radians(theta*0)))
        x12 = -((r-(coils * (b - total_space))) * sin(radians(theta/2)))

        print(round(x11, 2), round(y11, 2), file=f)
        print(round(x21, 2), round(y21, 2), file=f)
        print(round(x22, 2), round(y22, 2), file=f)
        print(round(x23, 2), round(y23, 2), file=f)
        print(round(x24, 2), round(y24, 2), file=f)
        print(round(x25, 2), round(y25, 2), file=f)
        print(round(x15, 2), round(y15, 2), file=f)
        print(round(x14, 2), round(y14, 2), file=f)
        print(round(x13, 2), round(y13, 2), file=f)
        print(round(x12, 2), round(y12, 2), file=f)

    # End point on the internal turn and begining point on external turn

    y11 = ((r - (last_internal_point * (b - total_space))) * cos(radians(theta)) + (last_internal_point * b))
    x11 = -((r - (last_internal_point * (b - total_space))) * sin(radians(theta)))
    print(round(x11, 2), round(y11, 2), file=f)

    # The external turn
    # Exchange formulas for small and big arcs

    for coils in ex_coil_no:
        y11 = ((r-((coils+1) * (b - total_space))+space)*cos(radians(theta))+((coils+1)*b)-c)
        x11 = -((r-((coils+1) * (b - total_space))+space)*sin(radians(theta)))

        y21 = ((R-(coils * (total_space + b))+c)*cos(radians(theta)))+(coils*b) - thickness
        y22 = ((R-(coils * (total_space + b))+c)*cos(radians(theta/2)))+(coils*b) - thickness
        y23 = ((R-(coils * (total_space + b))+c)*cos(radians(theta*0)))+(coils*b) - thickness
        y24 = ((R-(coils * (total_space + b))+c)*cos(radians(theta/2)))+(coils*b) - thickness
        y25 = ((R-(coils * (total_space + b))+c)*cos(radians(theta)))+(coils*b) - thickness

        y15 = ((r-(coils * (b - total_space)) + space)*cos(radians(theta)))+(coils*b) - c
        y14 = ((r-(coils * (b - total_space)) + space)*cos(radians(theta/2)))+(coils*b) - c
        y13 = ((r-(coils * (b - total_space)) + space)*cos(radians(theta*0)))+(coils*b) - c
        y12 = ((r-(coils * (b - total_space)) + space)*cos(radians(theta/2)))+(coils*b) - c

        x21 = -((R - (coils * (total_space + b))+c) * sin(radians(theta)))
        x22 = -((R - (coils * (total_space + b))+c) * sin(radians(theta/2)))
        x23 = ((R - (coils * (total_space + b))+c) * sin(radians(theta*0)))
        x24 = ((R - (coils * (total_space + b))+c) * sin(radians(theta/2)))
        x25 = ((R - (coils * (total_space + b))+c) * sin(radians(theta)))

        x15 = ((r-(coils * (b - total_space)) + space) * sin(radians(theta)))
        x14 = ((r-(coils * (b - total_space)) + space) * sin(radians(theta/2)))
        x13 = ((r-(coils * (b - total_space)) + space) * sin(radians(theta*0)))
        x12 = -((r-(coils * (b - total_space)) + space) * sin(radians(theta/2)))

        print(round(x11, 2), round(y11, 2), file=f)
        print(round(x12, 2), round(y12, 2), file=f)
        print(round(x13, 2), round(y13, 2), file=f)
        print(round(x14, 2), round(y14, 2), file=f)
        print(round(x15, 2), round(y15, 2), file=f)
        print(round(x25, 2), round(y25, 2), file=f)
        print(round(x24, 2), round(y24, 2), file=f)
        print(round(x23, 2), round(y23, 2), file=f)
        print(round(x22, 2), round(y22, 2), file=f)
        print(round(x21, 2), round(y21, 2), file=f)

    # Back to the start of the coil
    y11 = (r-total_space+space)*cos(radians(theta))-c
    x11 = -(r-total_space+space)*sin(radians(theta))
    print(round(x11, 2), round(y11, 2), file=f)

    # Start point to close the loop of the coil
    y11 = (r-total_space)*cos(radians(theta))
    x11 = -(r-total_space)*sin(radians(theta))
    print(round(x11, 2), round(y11, 2), file=f)
