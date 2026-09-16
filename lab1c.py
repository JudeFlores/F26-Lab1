# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: September 16, 2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1c.py

#TO-DO 1:
# import math module.
# Create a variable called 'radius' and take its value form user.
# Convert the variable to integer using int()
# use the contant pi form math module and compute the area of the circle using the variable 'radius'
import math
radius = input("Please enter an integer: ")
radius = int(radius)
area = math.pi*radius**2
print("%10.2f" % (area))