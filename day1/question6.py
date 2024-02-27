"""Question 1: Write a program that takes a user's input (a string) and checks if it contains the letter 'a'. If it does, print "Letter 
'a' found!", otherwise print "Letter 'a' not found!"."""

"""Create a program that asks the user to input their age. If the age is 18 or above, print "You are an adult." If the age is 
between 13 and 17 (inclusive), print "You are a teenager." If the age is below 13, print "You are a child." """


"""Create a program that simulates a basic ATM. The program should ask the user to enter the amount they want to withdraw. 
If the amount is less than the balance (assume balance is 1000), print "Here is your money". If the amount is more than the balance, 
print "Insufficient funds"."""

balance = 1000

user_input = int(input("Enter amount: "))

if user_input < balance:
    print("Here is your money")

else:
    print("Insufficient funds")