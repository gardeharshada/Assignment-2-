# Swap two numbers without using a third variable:
def swap_without_third_variable(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
a = 5
b = 10
a, b = swap_without_third_variable(a, b)
print("Swapped values", a, b)