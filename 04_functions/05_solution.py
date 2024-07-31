def greet(name = "User"):
    return "Hello, " + name + " !"

user_input = str(input("Enter the name: "))

print(greet(user_input))
print(greet())