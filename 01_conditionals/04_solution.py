fruit = str(input("Enter Fruit name: "))
color = str(input("Enter Color: "))

if fruit == "Banana":
    if color == "Green": 
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")
else:
    print("Missing Fruits")

     
