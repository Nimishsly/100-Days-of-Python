"""Write a Python program to check if a given number is positive, negative, or zero.
Create a program that checks whether a given number is even or odd using an if-else statement.
Write a function that takes in a number and returns "even" if it's divisible by 2, and "odd" otherwise.
Implement a program that checks if a user-inputted password is "strong" (at least 8 characters and includes both letters and numbers)."""


num = int(input("Enter number : "))

if num % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")