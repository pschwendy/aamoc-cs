"""
Exercise 7: Write a while loop that prints the first 5 numbers in the following pattern.
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5
"""
i = 1  # our first counter
while i <= 5:
    j = 1  # our second counter
    output = ""
    while j <= i:
        output += str(j) + " "
        j += 1
    print(output)
    i += 1

"""
This problem does something funky: we have a while loop inside another while loop! Similar to Exercise 3, where we wanted to print out the first 5 numbers on the same line, here we want to print out numbers on the same line, but with more each time until we reach 5.

To do this, we should model our program as if it were a table. We need a while loop to count the five rows, and a while loop to count each column within the row. 

       | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
Row 1: |   1   |   x   |   x   |   x   |   x   |
Row 2: |   1   |   2   |   x   |   x   |   x   |
Row 3: |   1   |   2   |   3   |   x   |   x   |
Row 4: |   1   |   2   |   3   |   4   |   x   |
Row 5: |   1   |   2   |   3   |   4   |   5   |

Looking at it this way, we can see that as our row number increases, our column number also increases (notice that we can ignore the gray columns as they do nothing). In other words, when we count our columns, we should only count UP TO our row number. This will come in handy later.

Now that we’ve thought a bit about the problem, let’s try to program it.
First, we need a while loop to count the five rows. Let’s call our counter i.
-----------------
i = 1
while i <= 5:
    i += 1
-----------------

Perfect. Now comes the tricky part: counting up to our row number (i) and putting all the numbers we count into a single line. Since we already used i, let’s call our second counter j, and just like in Exercise 3, let’s use strings to put our counts into the same line.
------------------------------------------------------------------------
j = 1
output = ""  # remember we want to start with nothing, or "" for strings
   while j <= i:  # here we're counting only up to our row number (i)
       output += str(j) + " "  # concatenating strings 
       j += 1
   print(output)
--------------------------------------------------------------------------

Now let’s put it all together with our second while loop inside the first. We go by each row, and at each row we count the columns up to that row’s number:
--------------------------------------------------------------------------
i = 1  # our first counter
while counter <= 5:  # count each row
    j = 1  # our second counter
    output = ""
    while j <= i:  # count each column up to the row number
        output += str(j) + " "
        j += 1
    print(output)
    i += 1
--------------------------------------------------------------------------
"""