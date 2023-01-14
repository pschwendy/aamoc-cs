# Exercise 4: Write a function that returns the highest value in a list of integers.
def max_value(nums: list) -> int:
    result = nums[0]
    for num in nums:
        if num > result:
            result = num
    return result