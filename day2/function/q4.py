#Implement a function called greet that takes a person's name as a parameter and prints "Hello, [name]!"""


def greet(name):
    return "Hello , " + name

name = input("Enter name: ")

result = greet(name)
print(result)