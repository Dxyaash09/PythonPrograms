# Grocery List with Prices

grocery_list = [
    ["Milk", 40],
    ["Bread", 30],
    ["Eggs", 60],
    ["Butter", 120]
]

print("Grocery List:")
for item, price in grocery_list:
    print(f"{item} - ₹{price}")

# Calculate total cost
total = sum(price for _, price in grocery_list)
print("\nTotal Cost: ₹", total)
