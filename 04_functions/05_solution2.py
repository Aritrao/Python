def greet(name="User"):
    return "Hello, " + name + " !"

# Taking input from user
user_input = str(input("Enter your name (or press Enter to use the default name): "))

# Check if the user provided a name or pressed Enter for the default name
if user_input.strip():  # If the user input is not empty
    print(greet(user_input))
else:  # If the user input is empty, use the default name
    print(greet())

