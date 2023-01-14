# Exercise 4: Write a while loop that finds the average of the first ten numbers.

counter = 1
summation = 0
while counter <= 10:
    summation += counter
    counter += 1

average = summation/10
print(average)


"""
Explanation: In order to calculate the average of the first ten numbers, we must add them all up and divide by 10. 

For the first part—adding them up—we create a while loop that adds our counter to a summation—starting at 0—and increases the counter by 1 each time. This gives us:
summation = 0 + 1 + 2 + 3 + …… + 9 + 10

For the second part, we calculate the average by dividing summation by 10. This should give us 5.5, the correct answer.
"""