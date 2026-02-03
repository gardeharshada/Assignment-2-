# Swap two numbers using a third variable:
def swap_using_third_variable(a, b):
    temp = a
    a = b
    b = temp
    return a, b
a = 5
b = 10
a, b = swap_using_third_variable(a, b)
print("Swapped values:", a, b)