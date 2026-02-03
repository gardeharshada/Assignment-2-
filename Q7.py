# Find the sum of a three-digit number:
def sum_of_digits(number):
    if 100 <= number <= 999:
        sum_digits = sum(int(digit) for digit in str(number))
        return sum_digits
    else:
        return "Enter a valid three-digit number."
    number = 123
    print("Sum of digits:", sum_of_digits(number))