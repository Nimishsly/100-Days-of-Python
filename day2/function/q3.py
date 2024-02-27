#Write a function that takes two numbers and returns the maximum of the two.

def Largetnumber(a,b):
    if a > b:
        return a
    else:
        return b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


result =  Largetnumber(a,b)

print("Largest number is ", result)