#  Reverse a three-digit number:
def reverse_number(number):
    if 100 <= number <= 999:
        return int(str(number)[::-1])
    else:
        return "Enter a valid three-digit number."
    number = 123
    print("Reversed number:", reverse_number(number))