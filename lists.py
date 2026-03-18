# lists_demo.py
# Demonstration of Python Lists

print("----- Creating a List -----")
numbers = [10, 20, 30, 40, 50]
print("numbers:", numbers)

# ---------------------------------------------------

print("\n----- Accessing Elements -----")
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])

# ---------------------------------------------------

print("\n----- Modifying Elements -----")
numbers[1] = 99
print("After modification:", numbers)

# ---------------------------------------------------

print("\n----- Adding Elements -----")

# append() adds element at end
numbers.append(60)
print("After append:", numbers)

# insert() adds element at specific position
numbers.insert(2, 25)
print("After insert at index 2:", numbers)

# ---------------------------------------------------

print("\n----- Removing Elements -----")

# remove() removes by value
numbers.remove(99)
print("After removing 99:", numbers)

# pop() removes by index
numbers.pop(3)
print("After pop index 3:", numbers)

# ---------------------------------------------------

print("\n----- Length of List -----")
print("Length:", len(numbers))

# ---------------------------------------------------

print("\n----- Looping Through List -----")
for num in numbers:
    print("Value:", num)

# ---------------------------------------------------

print("\n----- List Slicing -----")
print("First three elements:", numbers[:3])
print("Middle elements:", numbers[1:4])

# ---------------------------------------------------

print("\n----- Mixed Data Types -----")
mixed = [10, "apple", 3.14, True]
print("Mixed list:", mixed)

# ---------------------------------------------------

print("\n----- Nested Lists -----")
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Matrix:", matrix)
print("Element from matrix (row 2 col 3):", matrix[1][2])

# ---------------------------------------------------

print("\n----- List Comprehension -----")
squares = [x**2 for x in range(6)]
print("Squares:", squares)

# ---------------------------------------------------

print("\n----- Sorting Lists -----")
numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

# ---------------------------------------------------

print("\n----- Copying Lists -----")
copy_list = numbers.copy()
print("Copied list:", copy_list)

# ---------------------------------------------------

print("\n----- Checking if Element Exists -----")
if 40 in numbers:
    print("40 exists in the list")

# ---------------------------------------------------

print("\n----- End of List Demonstration -----")