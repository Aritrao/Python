number = int(input("Enter the numbers: "))
sum_even = 0

for i in range(1, number+1):
    if i%2 == 0:
        sum_even += 1

print("Sum of even number is:", sum_even)