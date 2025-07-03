""" Task2. Write a program that calculates the area of a rectangle, triangle and circle
(write three functions to calculate the area. And call them in the main program
depending on the user's choice)."""
import math

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * (radius ** 2)

def main():
    print("Area Calculator")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        length = float(input("Enter length of the rectangle: "))
        width = float(input("Enter width of the rectangle: "))
        area = rectangle_area(length, width)
        print(f"Area of the rectangle: {area}")
    elif choice == '2':
        base = float(input("Enter base of the triangle: "))
        height = float(input("Enter height of the triangle: "))
        area = triangle_area(base, height)
        print(f"Area of the triangle: {area}")
    elif choice == '3':
        radius = float(input("Enter radius of the circle: "))
        area = circle_area(radius)
        print(f"Area of the circle: {area:.2f}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
