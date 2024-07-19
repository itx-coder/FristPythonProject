# Define a dictionary of items in the shop with their prices
shop_items = {
    "apple": 0.99,
    "banana": 0.49,
    "orange": 1.29,
    "milk": 2.99,
    "bread": 1.99
}

# Initialize an empty shopping cart
cart = {}

# Display the shop items and prices
print("Welcome to the shop!")
print("Available items:")
for item, price in shop_items.items():
    print(f"{item}: ${price:.2f}")

# Loop until the user wants to checkout
while True:
    # Ask the user to add an item to the cart
    item = input("Enter an item to add to your cart (or 'done' to checkout): ")
    
    # If the user wants to checkout, break the loop
    if item.lower() == "done":
        break
    
    # Check if the item is in the shop
    if item in shop_items:
        # Add the item to the cart
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1
        print(f"Added {item} to your cart!")
    else:
        print(f"Sorry, we don't have {item} in stock.")

# Display the cart contents and total cost
print("Your cart:")
for item, quantity in cart.items():
    price = shop_items[item]
    total_cost = price * quantity
    print(f"{item} x {quantity}: ${total_cost:.2f}")
total_cost = 0
for item, quantity in cart.items():
    total_cost += shop_items[item] * quantity
print("Total cost: $%.2f" % total_cost)