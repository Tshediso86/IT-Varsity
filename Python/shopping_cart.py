#Create a shopping cart programme that will continiously ask the user the food product and the price of that product.
#Have an exit clause if the user wishes to stop adding more things to their cart.
#At the end show the food items and the total price of the items in the cart.

foods = []
prices = []

while True:
    food = input("Enter food product or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food} R"))
        foods.append(food)
        prices.append(price)

print("----- Your Cart ----")
for i in range(len(foods)):
    print(f"{foods[i]} - R{prices[i]:.2f}")
total = sum(prices)
print("\n")
print(f"Total price: R{total:.2f}")