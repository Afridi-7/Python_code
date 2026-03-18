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




# advanced_lists_demo

print("----- BASIC LIST -----")
nums = [10, 20, 30, 40, 50]
print(nums)


# ------------------------------------------------
print("\n----- INDEXING -----")

print("First element:", nums[0])
print("Last element:", nums[-1])
print("Second last:", nums[-2])


# ------------------------------------------------
print("\n----- SLICING -----")

print("First three:", nums[:3])
print("From index 2 onward:", nums[2:])
print("Middle slice:", nums[1:4])

# step slicing
print("Every second element:", nums[::2])
print("Reverse list:", nums[::-1])


# ------------------------------------------------
print("\n----- APPEND VS EXTEND -----")

a = [1,2,3]
b = [4,5,6]

a.append(b)
print("append:", a)

a = [1,2,3]
a.extend(b)
print("extend:", a)


# ------------------------------------------------
print("\n----- LIST CONCATENATION -----")

list1 = [1,2]
list2 = [3,4]

combined = list1 + list2
print("combined:", combined)


# ------------------------------------------------
print("\n----- LIST MULTIPLICATION -----")

zeros = [0] * 5
print("five zeros:", zeros)


# ------------------------------------------------
print("\n----- LOOP WITH INDEX -----")

names = ["Ali", "Sara", "John"]

for i, name in enumerate(names):
    print(i, name)


# ------------------------------------------------
print("\n----- NESTED LISTS -----")

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Matrix:", matrix)
print("Element (row1,col2):", matrix[0][1])


# ------------------------------------------------
print("\n----- LIST COMPREHENSION -----")

squares = [x*x for x in range(10)]
print("Squares:", squares)

even_numbers = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", even_numbers)


# ------------------------------------------------
print("\n----- NESTED LIST COMPREHENSION -----")

matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)


# ------------------------------------------------
print("\n----- COPYING LISTS -----")

original = [1,2,3]
copy1 = original
copy2 = original.copy()

copy1[0] = 999

print("original:", original)
print("copy1:", copy1)
print("copy2:", copy2)


# ------------------------------------------------
print("\n----- LIST METHODS -----")

numbers = [5,2,9,1,5,6]

numbers.sort()
print("sorted:", numbers)

numbers.reverse()
print("reversed:", numbers)

print("count of 5:", numbers.count(5))
print("index of 9:", numbers.index(9))


# ------------------------------------------------
print("\n----- REMOVING ELEMENTS SAFELY -----")

nums = [1,2,3,4,5]

while 3 in nums:
    nums.remove(3)

print(nums)


# ------------------------------------------------
print("\n----- UNPACKING LISTS -----")

a,b,c = [10,20,30]

print("a:", a)
print("b:", b)
print("c:", c)


# ------------------------------------------------
print("\n----- STAR UNPACKING -----")

first, *middle, last = [1,2,3,4,5]

print("first:", first)
print("middle:", middle)
print("last:", last)


# ------------------------------------------------
print("\n----- SORT WITHOUT CHANGING ORIGINAL -----")

nums = [4,1,7,2]

sorted_nums = sorted(nums)

print("original:", nums)
print("sorted:", sorted_nums)


# ------------------------------------------------
print("\n----- FILTERING LISTS -----")

nums = [1,2,3,4,5,6]

filtered = [x for x in nums if x > 3]

print(filtered)

