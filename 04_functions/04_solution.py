import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

number = int(input("Enter the Radius value: "))

area, circumference = circle_stats(number)

# print("Area:", area, "Circuference:", circumference)

# Print the results with two-digit precision
print(f"Area : { area:.2f}, Circumference : {circumference:.2f}")