Year = int(input("Enter the Year: "))

if (Year % 400 == 0) or (Year % 4 == 0 and Year % 100 != 0):
    print(Year, " is leap year")
else:
    print(Year, " is NOT a leap year")
    
 