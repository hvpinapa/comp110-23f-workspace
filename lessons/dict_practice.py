"""Practice with dictionaries!"""

# Constructing a dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Created my dictionary:")
print(ice_cream)

# Adding a key, value pair to the dictionary
ice_cream["mint"] = 3
print("Added mint to dictionary:")
print(ice_cream)

# Removing a key, value pair
ice_cream.pop("mint")
print("Removed mint:")
print(ice_cream)

# Accessing a value
print(f"There are {ice_cream['chocolate']} orders of chocolate")

# Adjusting a value
ice_cream["vanilla"] = 10
# ice_cream["vanilla"] += 2
print("After adjusting the amount of vanilla:")
print(ice_cream)

# Getting the length
print(f"The number of key-value pairs: {len(ice_cream)}")

# Checking if a value is in a dictionary
print("Is chocolate in ice_cream?")
print("chocolate" in ice_cream)
print("Is mint in ice_cream?")
print("mint" in ice_cream)

# Using "in" in a conditional
if "mint" in ice_cream:
    print(f"Number of orders: {ice_cream['mint']}")
else:
    print("No orders of mint!")

# Loops through and prints every flavor and its number of orders
for key in ice_cream:
    # print "<flavor> has <num_orders> orders"
    print(f"{key} has {ice_cream[key]} orders.")