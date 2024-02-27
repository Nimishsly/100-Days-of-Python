"""Question 2:
Create a Python program to determine the grading of students based on their marks. The program should take the marks as input and print the corresponding grade according to the following criteria:

90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F """

marks = int(input("Enter Marks: "))

if(marks >= 90):
    print("Good job!! you got A grade")

elif(marks > 89 and marks < 80):
    print("You got B grade")

elif(marks > 70 and marks < 79):
    print("Study hard, You got C grade")

elif(marks > 60 and marks < 69):
    print("Bring your parents, You got D grade")

elif(marks < 60):
    print("You are failed, F grade")

else:
    print("Invalid Marks")