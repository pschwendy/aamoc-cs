# Exercise 2, Part 1: Create a function that counts the number of odd values in a list of integers.
def count_odd(nums: list) -> int:
    count = 0
    for num in nums:
        if num % 2 == 1:
            count += 1
    return count

# Part 2: Create a function that prints all the odd values in a list as a list
def count_odd_return_list(nums: list) -> list:
    result = []
    for num in nums:
        if num % 2 == 1:
            result.append(num)
    return result