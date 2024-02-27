
import datetime

# Get the current hour
current_hour = datetime.datetime.now().hour

# Greet the user based on the current hour
if 5 <= current_hour < 12:
    print("Good morning!")
elif 12 <= current_hour < 18:
    print("Good afternoon!")
elif 18 <= current_hour < 22:
    print("Good evening!")
else:
    print("Good night!")
