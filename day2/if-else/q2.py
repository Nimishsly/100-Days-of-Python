#Implement a program that checks if a user-inputted password is "strong" (at least 8 characters and includes both letters and numbers)."""

passwd = input("Enter password: ")

if len(passwd)>=8 and any(char.isdigit() for char in passwd) and any(char.isalpha() for char in passwd):
    print("Correct password")

else:
    print("Password should contain at least 8 characters and includes both letters and numbers")