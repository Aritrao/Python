numbers = input("Enter Numbers Seperated by spaces: ")
positive_number_count = 0
negative_number_count = 0

# Split the input string into individual number strings
number_list = numbers.split()

# Iterate through the list of number strings
for num_str in number_list:
    num = int(num_str)  # Convert each number string to an integer
    if num > 0:
        positive_number_count += 1
    elif num < 0:
        negative_number_count += 1
print("Your Positive Number Count: ",positive_number_count)
print("Your Negative Number Count: ",negative_number_count)