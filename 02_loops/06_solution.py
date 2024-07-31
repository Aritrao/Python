# factorial of 5 is = 5*4*3*2*1
number = int(input("Enter The Number: "))
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1
          
print("Factorial value of number is:", factorial)