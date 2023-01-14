# part a
def max(a, b):
    if a > b:
        return a
    else:
        return b

# part b
def max_of_three1(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

# part b -- using max(a, b) from part a
def max_of_three2(a, b, c):
    return max(max(a, b), c)