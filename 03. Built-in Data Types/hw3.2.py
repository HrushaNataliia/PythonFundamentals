"""A four-digit natural number is specified:
- find the product of the digits of this number
- write the number in reverse order
- in ascending order, you need to sort the numbers included in the given number"""

while True:
    num = input("Enter a four-digit natural number: ")
    if num.isdigit() and len(num) == 4:
        num = int(num)
        break
    print("Invalid input. Please enter a four-digit natural number.")

digits = [int(d) for d in str(num)]

product = digits[0] * digits[1] * digits[2] * digits[3]

reversed_num = int(str(num)[::-1])

sorted_num = int(''.join(map(str, sorted(digits))))

print(f"product: {product}")
print(f"reversed_num: {reversed_num}")
print(f"sorted_num: {sorted_num}")

