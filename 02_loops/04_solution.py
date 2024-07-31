string = str(input("Enter The String: "))
reversed_str = ""

for char in string:
    reversed_str = char + reversed_str

print("Your Reversed String is" ,reversed_str)