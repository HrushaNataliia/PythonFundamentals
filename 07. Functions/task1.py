""" Task1. Write a function that returns the largest number of two numbers
(use DocStrings documentation strings in the function)."""

def largest_num(num1, num2):
    """
    Returns the largest of two given numbers.
    Parameters:
        num1 (int/float): The first number.
        num2 (int/float): The second number.
    Returns:
        int/float: The larger of the two numbers.
    """
    if num1 > num2:
        return num1
    else:
        return num2

print(largest_num(-5,5.25))

