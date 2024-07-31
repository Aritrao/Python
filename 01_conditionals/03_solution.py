score = int(input("Enter the Student's score: "))

if score >=101:
    print("Please verify your score again")
    exit()
    
if score >= 90:
    print("A Grade")
elif score >= 80:
    print("B Grade")
elif score >= 70:
    print("C Grade")
elif score >= 60:
    print("D Grade")
else:
    print("F Grade") 

