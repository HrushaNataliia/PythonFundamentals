"""Task1. Create a list that contains elements of integer type, then use
the loop to change the type of these elements to a floating type.
(Hint: use the built-in float () function)."""

int_list = [1, 2, 3, 4, 5]
for i in range(len(int_list)):
    int_list[i] = float(int_list[i])
print(int_list)

