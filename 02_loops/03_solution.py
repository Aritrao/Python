number = int(input("EnterThe Numbers: "))

for i in range(1, 11):
    if i == 5:
        continue
    print(number, "x", i, "=", number*i )