def even_generator(limit):
    for i in range(2, limit + 1, 2):            
      yield i

user_input = int(input("Enter the Numbers: "))
   
print("All the Even Number in the range"  , user_input , "is:" ,)
for num in even_generator(user_input):       
    print(num)
   