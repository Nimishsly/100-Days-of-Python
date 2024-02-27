#Create a function that takes a list of numbers as input and returns the sum of those numbers.

def sum_of_numbers(user_list):
    total = 0
    for num in user_list:
        total += num
    return total

# Taking a list as user input
input_string = input("Enter elements of the list separated by space: ")

# Splitting the input string by space to get individual elements
# Converting each element to integer assuming they are numbers
user_list = [int(item) for item in input_string.split()]

result = sum_of_numbers(user_list)
print("Sum of numbers:", result)


