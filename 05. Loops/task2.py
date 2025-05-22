"""Task2. Print Fibonacci numbers up to the entered number n,
using cycles.
(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)"""

n = int(input("Enter a number: "))
a, b = 0, 1

print("Fibonacci sequence up to", n, ":")
while a <= n:
    print(a, end=' ')
    a, b = b, a + b