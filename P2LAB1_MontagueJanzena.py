# Janzena Montague
# October 6, 2026
# P2LAB1
# This program calculates the diameter, circumference, and area of a circle using a radius entered by the user.

import math

# Pseudocode:
# Get the radius from the user
# Calculate the diameter using the radius
# Calculate the circumference using the radius and pi
# Calculate the area using the radius and pi
# Display the diameter, circumference, and area


radius = float(input("What is the radius of the circle: "))
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"The diameter of the circle is: {diameter:.1f}")
print(f"The circumference of the circle is: {circumference:.2f}")
print(f"The area of the circle is: {area:.3f}")