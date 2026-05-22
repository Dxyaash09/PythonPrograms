# Search in a List

names = ["Alice", "Bob", "Charlie", "David", "Eva"]

search_name = input("Enter a name to search: ")

if search_name in names:
    print(f"{search_name} is in the list!")
else:
    print(f"{search_name} not found.")
