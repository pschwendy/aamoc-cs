"""
Exercise 2:
1) Write a function to find value 20 in the list, and if it is present, replace it with 200.
2) Now only update the first 20 in the list.
"""
def change_20_into_200(l: list):
    i = 0
    while i < len(l):
        if l[i] == 20:
            l[i] = 200
        i += 1
    return l

def change_first_20_into_200(l: list):
    i = 0
    while i < len(l):
        if l[i] == 20:
            l[i] = 200
            break
        i += 1
    return l

print(change_20_into_200([1, 2, 20, 5, 3, 20]))
print(change_first_20_into_200([1, 2, 20, 5, 3, 20]))