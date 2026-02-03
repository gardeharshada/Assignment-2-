# WAP to calculate the total salary of an employee based on basic, DA, TA, and HRA:
def calculate_salary(basic_salary):
    da = 0.10 * basic_salary
    ta = 0.12 * basic_salary
    hra = 0.15 * basic_salary
    total_salary = basic_salary + da + ta + hra
    return total_salary
basic_salary = 5000
print("Total salary:", calculate_salary(basic_salary))