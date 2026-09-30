# Loop through numbers 1 to 100
for i in range(1, 101):
# Checking if the numbers are divisible by both 3 and 5

    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        
#Checking if the numbers are divisible by 3
    elif i % 3 == 0:
        print("fizz")

#Checking if the numbers are divisible by 5    
    elif i % 5 == 0:
        print("buzz")

# If neither of the conditions are met, then just print the number
    else:
        print(i)