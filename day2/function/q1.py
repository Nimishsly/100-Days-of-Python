"""Function Questions
Write a Python function to calculate the area of a rectangle (given its length and width).
Create a function that takes a list of numbers as input and returns the sum of those numbers.
Write a function that takes two numbers and returns the maximum of the two.
Implement a function called greet that takes a person's name as a parameter and prints "Hello, [name]!"""

def Areaofrect(l ,b):
    return l * b

l = int(input("Enter length: "))
b = int(input("Enter Breadth: "))

area = Areaofrect(l ,b)

print("Area of Rectangle is ", area)


