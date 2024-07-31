def multiply(p1, p2):
    if isinstance(p1, (int, float)) and isinstance(p2, (int, float)):
        return p1 * p2
    elif isinstance(p1, str) and isinstance(p2, int):
        return p1 * p2
    elif isinstance(p2, str) and isinstance(p1, int):
        return p2 * p1
    else:
        raise ValueError("Invalid input types. Function accepts (number, number) or (string, integer).")

# Function to determine the type of the input
def determine_type(value):
    try:
        return int(value)
    except ValueError:
        return value

# Taking input from user
value1 = input("Enter value 1 (int or str): ")
value2 = input("Enter value 2 (int or str): ")

# Determine the type of each input
value1 = determine_type(value1)
value2 = determine_type(value2)

# Multiply the values and print the result
try:
    result = multiply(value1, value2)
    print("Multiplication Value is:", result)
except ValueError as e:
    print(e)
