""" Task2.
Write a Python program to check the validity of a password (input from users).
Validation:
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters."""

import re


def validate_password(password):
    errors = []

    if len(password) < 6:
        errors.append("Password must be at least 6 characters long.")
    elif len(password) > 16:
        errors.append("Password must not exceed 16 characters.")

    if not re.search("[a-z]", password):
        errors.append("Password must contain at least one lowercase letter (a-z).")

    if not re.search("[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter (A-Z).")

    if not re.search("[0-9]", password):
        errors.append("Password must contain at least one digit (0-9).")

    if not re.search("[$#@]", password):
        errors.append("Password must contain at least one special character ($, #, or @).")

    if errors:
        print("\nPassword is invalid. Reasons:")
        for error in errors:
            print(f"- {error}")
        return False
    else:
        print("Password is valid!")
        return True


password = input("Enter password: ")
validate_password(password)
