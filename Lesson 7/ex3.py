# Exercise 3, Part 1: Write a while loop that prints the first 5 numbers on the same line (12345).
i = 1
result = ""
while i <= 5:
    result += str(i)
    i += 1
print(result)

# Option 2
i = 1
while i <= 5:
    print(i, end="")
    i += 1
print()

# Part 2: Write a program that asks the user for a number n, then prints the first n numbers on the same line (12…n).
n = input()
i = 1
result = ""
while i <= n:
    result += str(i)
    i += 1
print(result)