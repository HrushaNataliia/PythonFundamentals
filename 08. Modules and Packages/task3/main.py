"""Task3.
Write a program that calculates the area of a rectangle $$S=a*b$$, the area of a
triangle $$S=0.5*h*a$$, the area of a circle $$S=pi*r**2$$. This module must be used in
another module in which we ask the user the area of which figure he wants to
calculate.
(To perform the task, you need to import the math module, and from it the
pow() function and the value of the variable pi, and module, which contains
three functions for finding areas, into the main program. The basic logic of the
program is executed in the main module)."""

from geometry import rectangle_area, triangle_area, circle_area


def main():
    print("Area Calculator")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Select figure (1-3): ")

    if choice == '1':
        a = float(input("Enter length (a): "))
        b = float(input("Enter width (b): "))
        print(f"Rectangle area: {rectangle_area(a, b)}")
    elif choice == '2':
        h = float(input("Enter height (h): "))
        a = float(input("Enter base (a): "))
        print(f"Triangle area: {triangle_area(h, a)}")
    elif choice == '3':
        r = float(input("Enter radius (r): "))
        print(f"Circle area: {circle_area(r)}")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
