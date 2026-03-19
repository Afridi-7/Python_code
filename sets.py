s1 = {1, 2, 3, 4}
print("Set:", s1)

# duplicates automatically removed
s2 = {1, 2, 2, 3, 3, 4}
print("No duplicates:", s2)

# empty set (IMPORTANT: not {})
empty = set()
print("Empty set:", empty)


# ------------------------------------------------
print("\n----- ADDING ELEMENTS -----")

s = {1, 2, 3}

s.add(4)
print("After add:", s)

# add multiple elements
s.update([5, 6, 7])
print("After update:", s)


# ------------------------------------------------
print("\n----- REMOVING ELEMENTS -----")

s = {1, 2, 3, 4}

s.remove(2)   # error if not found
print("After remove:", s)

s.discard(10) # no error
print("After discard (safe):", s)

removed = s.pop()  # removes random element
print("Popped:", removed)
print("After pop:", s)


# ------------------------------------------------
print("\n----- SET OPERATIONS -----")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# union
print("Union:", A | B)

# intersection
print("Intersection:", A & B)

# difference
print("A - B:", A - B)

# symmetric difference
print("Symmetric diff:", A ^ B)


# ------------------------------------------------
print("\n----- METHODS VERSION -----")

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference:", A.difference(B))


# ------------------------------------------------
print("\n----- CHECKING MEMBERSHIP -----")

print(3 in A)   # True
print(10 in A)  # False


# ------------------------------------------------
print("\n----- LOOPING THROUGH SET -----")

for item in A:
    print(item)


# ------------------------------------------------
print("\n----- SET COMPREHENSION -----")

nums = {x*x for x in range(6)}
print("Squares:", nums)


# ------------------------------------------------
print("\n----- SUBSET / SUPERSET -----")

A = {1, 2}
B = {1, 2, 3, 4}

print("A subset of B:", A.issubset(B))
print("B superset of A:", B.issuperset(A))


# ------------------------------------------------
print("\n----- REMOVING DUPLICATES FROM LIST -----")

lst = [1,2,2,3,3,4,5]

unique = list(set(lst))
print("Unique list:", unique)


# ------------------------------------------------
print("\n----- FROZEN SET (IMMUTABLE) -----")

fs = frozenset([1,2,3])
print("Frozen set:", fs)

# fs.add(4)  # ERROR (immutable)


# ------------------------------------------------
print("\n----- IMPORTANT PROPERTIES -----")

s = {1,2,3}

# sets are unordered
print("Set:", s)

# cannot access by index
# print(s[0])  # ERROR


# ------------------------------------------------
print("\n----- REAL USE CASE: FAST LOOKUP -----")

nums = [1,2,3,4,5,6,7,8,9]
lookup = set(nums)

print("Is 5 in list?", 5 in nums)     # slower
print("Is 5 in set?", 5 in lookup)   # faster


