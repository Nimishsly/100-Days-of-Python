"""Question 3:
Write a Python program to find the largest of three numbers. The program should take three numbers as input from the user and print the largest number."""

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 >= number2 and number1 >= number3:
    largest = number1

elif number2 >= number1 and number2 >= number3:
    largest = number2

else:
    largest = number3

print("Largest number is ", largest)