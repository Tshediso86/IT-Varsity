try:
    print(x)
except NameError:
    print("Something went wrong.")
else:
    print("Everthing went wrong.")
    
    
    x= -1
    if x < 0:
        raise Exception("No negative numbers allowed.")