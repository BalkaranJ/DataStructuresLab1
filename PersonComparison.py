from Person import Person
from PersonComparator import PersonComparator

print("Welcome to Comparing Objects Using Generics")

# Step 6: Sort by data using Comparable
persons = [
    Person("Ana", 25, "Anders"),
    Person("Howard", 30, "Mwangi"),
    Person("John", 20, "Yorres")
]

print("\n// Test cases for Comparable")
print("Step 6: Sorted by Data (Comparable):")
for p in sorted(persons):
    print(f"{p.get_name()} ► {p.get_data()} ► {p.get_age()}")

# Step 8: Sort by name using Comparator
print("\n// Test cases for Comparator")
print("Step 8: Sorted by Name (Comparator):")
for p in sorted(persons, key=PersonComparator.by_name):
    print(f"{p.get_name()} ► {p.get_data()} ► {p.get_age()}")

# Step 10: Sort by data with different data types (integers)
persons_diff = [
    Person("Frank", 31, 25),
    Person("Eve", 28, 30),
    Person("David", 35, 42)
]

print("\n// Test cases for Comparable")
print("Step 10: Sorted by Data (Comparable) for Different Data Types:")
for p in sorted(persons_diff):
    print(f"{p.get_name()} ► {p.get_data()} ► {p.get_age()}")

# Step 12: Sort by age when names are the same
persons_age = [
    Person("Alice", 30, "Data1"),
    Person("Alice", 28, "Data5"),
    Person("Bob", 25, "Data2"),
    Person("Charlie", 40, "Data3"),
    Person("David", 35, "Data4")
]

print("\n// Test cases to sort by the Age when names are the same")
print("Step 12: Sorted by Age (when names are the same):")
for p in sorted(persons_age, key=PersonComparator.by_age_when_same_name):
    print(f"{p.get_name()} ► {p.get_data()} ► {p.get_age()}")

# Testing exception handling
p1 = Person("Alice", 30, "StringData")
p2 = Person("Bob", 25, 42)

try:
    print(p1 == p2)
except TypeError as e:
    print(f"Exception caught: {e}")