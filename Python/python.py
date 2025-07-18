#Loop control statements

fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "cherry":
        break  # Exit the loop if cherry is found
    print(fruit)  # This will print apple, cherry, and date
    
    print()
    fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "cherry":
        pass  # Do nothing if cherry is found 
    print(fruit)