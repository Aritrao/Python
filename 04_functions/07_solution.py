def sum_of_args(*args):
    return sum(args)

# Take input from user
user_input = input("Enter numbers separated by spaces: ")

# Split the input string into individual number strings
numbers = user_input.split()

# Convert the number strings into integers
numbers = [int(num) for num in numbers]

# Pass the numbers to the function using argument unpacking
# result = sum_of_args(*numbers)

print("The sum is:", sum_of_args(*numbers))
