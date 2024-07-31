#Here we getting output in the form of list not normal way not using yield
def even_generator(limit):
    li = []
    for i in range(2, limit + 1, 2):
        li.append(i)
    return li

user_input = int(input("Enter the Numbers: "))

print("All the Even Number in the range"  , user_input , "is" , even_generator (user_input))