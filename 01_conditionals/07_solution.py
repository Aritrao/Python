order_size = str(input("Enter the order size: "))
extra_shot = str(input("Extrashot yes or not: "))

if extra_shot == "Yes":
    coffee = order_size + " coffee with an extra shot"
elif extra_shot == "No":
    coffee = order_size + " coffee"

print("Order: ",coffee)
