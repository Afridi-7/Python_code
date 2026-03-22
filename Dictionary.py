# =========================
# PYTHON DICTIONARY GUIDE
# =========================

# 1. Creating a dictionary
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

print("Initial dictionary:", student)


# 2. Accessing values
print("\nAccessing values:")
print("Name:", student["name"])
print("Age:", student.get("age"))  # safer way


# 3. Adding new key-value pair
student["city"] = "New York"
print("\nAfter adding city:", student)


# 4. Updating values
student["age"] = 21
print("\nAfter updating age:", student)


# 5. Deleting items
del student["grade"]
print("\nAfter deleting grade:", student)


# 6. Looping through dictionary
print("\nLooping through dictionary:")

print("Keys:")
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value pairs:")
for key, value in student.items():
    print(key, ":", value)


# 7. Safe access using get()
print("\nSafe access:")
print("Salary:", student.get("salary"))  # returns None instead of error


# 8. Word count example
print("\nWord count example:")

text = "cat dog cat bird dog cat"
words = text.split()

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print("Word count:", count)


# 9. Nested dictionary
print("\nNested dictionary:")

students = {
    "s1": {"name": "John", "age": 20},
    "s2": {"name": "Alice", "age": 22}
}

print("Student s1 name:", students["s1"]["name"])


# 10. Dictionary with list
print("\nDictionary with list:")

data = {
    "numbers": [1, 2, 3, 4],
    "letters": ["a", "b", "c"]
}

print("Numbers:", data["numbers"])
print("First letter:", data["letters"][0])


# 11. Dictionary comprehension
print("\nDictionary comprehension:")

squares = {x: x*x for x in range(5)}
print("Squares:", squares)


# 12. Check key existence
print("\nCheck key existence:")

if "name" in student:
    print("Key 'name' exists")


# 13. Length of dictionary
print("\nLength of dictionary:")
print(len(student))


# 14. Clear dictionary
temp = {"a": 1, "b": 2}
temp.clear()
print("\nAfter clear:", temp)


# =========================
# END
# =========================