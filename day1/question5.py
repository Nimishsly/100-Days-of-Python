"""Write a Python program that takes a sentence as input from the user. The program should then:

Check if the sentence contains the word "Python".
If it does, count the number of times "Python" appears in the sentence and print the count.
If it doesn't contain "Python", reverse the sentence and print it."""

user_input = input("Enter any sentence: ")

if "Python" in user_input:
    count = user_input.count("Python")  # Count the occurrences of "Python"
    print(f"The sentence contains 'Python' {count} times.")

else:
    reversed_sentence = user_input[::-1]  # Reverse the sentence
    print("Reversed sentence:", reversed_sentence)
