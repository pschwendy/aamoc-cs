"""
Exercise 4: Write a program that computes the factorial of a number inputted by the user.

As a reminder, factorial (!) means the product of all positive numbers less than or equal to a number. For example, 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720.
"""
n = int(input("To use the factorial calculator, pick a number: "))
i = 1  # i is our counter
n_factorial = 1
while i <= n:
    n_factorial *= i
    i += 1

print(f"{n}! = {n_factorial}")