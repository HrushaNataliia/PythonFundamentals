"""Interchange the values of two variables without using the third variable."""


a = input("Enter the first variable (a): ")     
b = input("Enter the second variable (b): ")

print(f"Before swapping: a = {a}, b = {b}")

a, b = b, a 

print(f"After swapping: a = {a}, b = {b}")

