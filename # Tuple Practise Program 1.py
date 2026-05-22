# Tuple Practise Program 1

# Create a tuple
fruits = ("Apple", "Banana", "Cherry", "Mango")

# Print the tuple
print("Fruits Tuple:", fruits)

# Access elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Loop through tuple
print("\nAll fruits:")
for fruit in fruits:
    print("-", fruit)

# Check membership
if "Banana" in fruits:
    print("\nBanana is in the tuple!")

# Tuple length
print("Number of fruits:", len(fruits))

# Nested tuple
nested_tuple = ("Numbers", (1, 2, 3))
print("\nNested Tuple:", nested_tuple)
print("Access nested element:", nested_tuple[1][2])

# Convert tuple to list (to modify)
fruits_list = list(fruits)
fruits_list.append("Orange")
print("\nModified List:", fruits_list)

# Convert back to tuple
fruits = tuple(fruits_list)
print("Updated Tuple:", fruits)
