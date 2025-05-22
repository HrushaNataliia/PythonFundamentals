"""Task3. Write a script that will calculate the factorial of the entered
number without using recursion.
Example: 0!=1, 1!=1, 2!=2, 3!= 1*2*3=6, ...."""

num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial doesn't exist for negative numbers")
elif num == 0:
    print("0! = 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"{num}! = {factorial}")