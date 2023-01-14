"""
Create a program that outputs a letter grade based on a given score.

An A is given if the grade is ≥ 90
A B is given if the grade is ≥ 80 but < 90
A C is given if the grade is ≥ 70 but < 80
A D is given for grades ≥ 60 but < 70
An E given for grades < 60
"""

grade = input()

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")