# Exercise 3: Create a function that returns the sum of integers in a list.
def find_sum(nums: list) -> int:
    result = 0
    for num in nums:
        result += num
    return result