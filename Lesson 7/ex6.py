"""
Exercise 6: Write a program that takes in input, asking if the program should shut down. 
If the user responds “y”, end the program. If the user responds “n”, ask again. Otherwise, print “Invalid input”.
"""
while True:
    shut_down = input("Should the program shut down (y/n)? ")
    if shut_down == "y":
        # break is a way to escape while loops
        break
    elif shut_down == "n":
        # continue allows you to skip to the next iteration in the while loop
        continue
    else:
        print("Invalid input")



"""
Explanation: Be careful here because we’re using a while True loop, which will run forever if we don’t write it properly. We’re also using two new keywords in this problem: break and continue. So what do these do?

break - the break keyword allows us to exit a while loop. When it is used, the while loop will immediately end without completing any of the code after (within the loop).
For example,
-----------------
while True:
    print("Hi!")
    break
    print("Bye!")
-----------------
The code above will print “Hi” and then immediately exit the loop. It will not print “Bye!”

continue -  the continue keyword continues to the next iteration of the while loop without completing any of the code after it (within the loop).

For example,
-----------------
i = 1
while i <= 5:
    print("Hi!")
    i += 1
    continue
    print("Bye!")
-----------------

The code above will print “Hi!” 5 times without ever printing “Bye!”. The continue keyword will immediately skip to the next iteration (notice that we’re still adding 1 to i before we reach the continue keyword).

Now, back to our problem. We can start by creating an infinite loop that takes in input at each iteration:
-------------------------------------------------------------
while True:
    shut_down = input("Should the program shut down (y/n)? ")
-------------------------------------------------------------

But before we try to run this, we should note that this is an infinite loop and will never end—not good! To exit the loop, we can use the break keyword if the user inputs “y”. Once again, we can check if the user inputs “y” with an if statement.
-------------------------------------------------------------
while True:
    shut_down = input("Should the program shut down (y/n)? ")
    if shut_down == "y":
        break
-------------------------------------------------------------


Now that we can check when the user inputs “n” or any other input, we can use elif and else.
-------------------------------------------------------------
while True:
    shut_down = input("Should the program shut down (y/n)? ")
    if shut_down == "y":
        break
   elif shut_down == "n":
       continue
   else:
       print("Invalid input")
-------------------------------------------------------------
"""