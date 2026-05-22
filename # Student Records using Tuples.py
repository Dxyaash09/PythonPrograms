# Student Records using Tuples

students = [
    ("Alice", 20, "Physics"),
    ("Bob", 22, "Math"),
    ("Charlie", 21, "Computer Science")
]

print("Student Records:")
for name, age, subject in students:
    print(f"Name: {name}, Age: {age}, Subject: {subject}")
