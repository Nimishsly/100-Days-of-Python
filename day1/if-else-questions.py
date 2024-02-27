"""Question 1:
Write a Python program to check if a number is positive, negative, or zero. The program should take user input and print the result.


Question 3:
Write a Python program to find the largest of three numbers. The program should take three numbers as input from the user and print the largest number."""


number =  int(input("Enter number: "))
if(number > 0):
    print("Positive number")

elif(number < 0):
    print("Negative number")


elif(number == 0):
    print("Number is zere")

else:
    print("Invalid input")

