pet_name = str(input("Enter Your pets name: "))
pet_age = int(input("Enter your pets age: "))

if pet_name == "Dog":
    if pet_age < 2:
        Food = "Puppy Food"
    else:
        Food = "Adult Food"
elif pet_name == "Cat":
    if pet_age <= 5:
        Food = "Junoir Cat Food"
    else:
        Food = "Senior Cat Food"

print("AI Suggest you ",Food)
