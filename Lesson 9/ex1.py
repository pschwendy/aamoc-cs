"""
Exercise 1: Write a function that takes in a list of integers and modifies the list so that each number is squared. 

Then test that function with the following lists:
a) [1, 2, 3, 4, 5]
b) [-2, 4, 8]

Note: use the ** operator for powers.
"""

def square_list(nums):
    x = 0
    while x < len(nums):
        nums[x] = nums[x] ** 2
        x += 1
    return nums

print(square_list([1, 2, 3, 4, 5]))
print(square_list([-2, 4, 8]))