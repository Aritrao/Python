number = int(input("Enter the number: "))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("The Number is NOT a Prime number")
            break
        else:
            print("Number is a Prime Number")
            break
else:
    print("The number is NOT a Prime Number")           