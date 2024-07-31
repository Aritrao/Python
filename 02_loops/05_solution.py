# for non repeated charecter
string = str(input("Enter the String: "))

for char in string:
    if string.count(char) == 1:
        print("Non Repeated Char is:", char)
        