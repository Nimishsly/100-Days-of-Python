"""Break Questions

Create a loop that iterates through a list of numbers, and if it finds a negative number, it stops the loop using break.
Write a program that takes a list of integers and finds the first occurrence of a number greater than 10, then stops.
"""

numbers = [12,56,30,-18,44,13]

for number in numbers:
    if number < 0:
        print("Found negative number", number)
        continue
    else:
        print(number)