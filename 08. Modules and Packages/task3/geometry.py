from math import pi, pow

def rectangle_area(a, b):
    """Calculates area of rectangle: S = a * b"""
    return a * b

def triangle_area(h, a):
    """Calculates area of triangle: S = 0.5 * h * a"""
    return 0.5 * h * a

def circle_area(r):
    """Calculates area of circle: S = π * r²"""
    return pi * pow(r, 2)
