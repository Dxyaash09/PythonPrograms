# Simple List Program

# Create a list of items
shopping_list = ["Milk", "Bread", "Eggs", "Butter"]

# Print the list
print("My Shopping List:")
for item in shopping_list:
    print("-", item)

# Add a new item
shopping_list.append("Cheese")
print("\nUpdated Shopping List:")
for item in shopping_list:
    print("-", item)

# Remove an item
shopping_list.remove("Eggs")
print("\nAfter Removing Eggs:")
for item in shopping_list:
    print("-", item)

# Access a specific item
print("\nFirst item on the list is:", shopping_list[0])
