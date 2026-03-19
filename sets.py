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

# ------------------------------------------------
print("\n----- SET VS LIST SPEED DEMO -----")

import time

big_list = list(range(1000000))
big_set = set(big_list)

start = time.time()
999999 in big_list
print("List check time:", time.time() - start)

start = time.time()
999999 in big_set
print("Set check time:", time.time() - start)

#------------------------------------------------

print("----- HASHABLE VS NON-HASHABLE -----")

# sets can only store HASHABLE (immutable) types
valid = {1, "hello", (1,2)}
print("Valid set:", valid)

# invalid example
try:
    bad = {[1,2], [3,4]}  # lists are mutable → not allowed
except TypeError as e:
    print("Error:", e)


# ------------------------------------------------
print("\n----- WHY HASHABLE MATTERS -----")

# sets use hashing (like dictionaries)
# that's why lookup is fast

s = {10, 20, 30}
print("Hash lookup example:", 20 in s)


# ------------------------------------------------
print("\n----- REMOVING DUPLICATES (ORDER PRESERVED TRICK) -----")

lst = [1,2,2,3,4,3,5]

# normal set destroys order
print("Using set:", list(set(lst)))

# better way (preserves order)
seen = set()
result = []

for x in lst:
    if x not in seen:
        seen.add(x)
        result.append(x)

print("Order preserved:", result)


# ------------------------------------------------
print("\n----- INTERSECTION OF MULTIPLE LISTS -----")

a = [1,2,3,4]
b = [3,4,5,6]
c = [4,5,6,7]

common = set(a) & set(b) & set(c)
print("Common elements:", common)


# ------------------------------------------------
print("\n----- FIND UNIQUE ELEMENTS BETWEEN LISTS -----")

a = [1,2,3]
b = [3,4,5]

unique = set(a) ^ set(b)
print("Unique elements:", unique)


# ------------------------------------------------
print("\n----- SET COMPARISONS -----")

A = {1,2,3}
B = {1,2,3,4}

print("A < B:", A < B)   # subset
print("B > A:", B > A)   # superset


# ------------------------------------------------
print("\n----- DISJOINT SETS -----")

A = {1,2,3}
B = {4,5,6}

print("No common elements:", A.isdisjoint(B))


# ------------------------------------------------
print("\n----- MODIFYING SET DURING LOOP (DANGER) -----")

s = {1,2,3,4}

try:
    for x in s:
        if x == 2:
            s.remove(x)  # bad idea
except RuntimeError as e:
    print("Error:", e)

# safe way
s = {1,2,3,4}
for x in s.copy():
    if x == 2:
        s.remove(x)

print("Safe removal:", s)


# ------------------------------------------------
print("\n----- SET OF OBJECTS (ADVANCED) -----")

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Ali")
p2 = Person("Ali")

people = {p1, p2}

print("Set of objects:", people)

# both exist because objects are different in memory


# ------------------------------------------------
print("\n----- CUSTOM HASH (VERY ADVANCED) -----")

class User:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

u1 = User("Ali")
u2 = User("Ali")

users = {u1, u2}

print("Custom hash removes duplicates:", users)


# ------------------------------------------------
print("\n----- USING SET FOR FAST FILTERING -----")

data = list(range(100000))
remove = {10, 200, 5000}

filtered = [x for x in data if x not in remove]
print("Filtered sample:", filtered[:10])


# ------------------------------------------------
print("\n----- POWER MOVE: SET FOR GRAPH PROBLEMS -----")

graph = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A"},
    "D": {"B"}
}

visited = set()

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    print("Visited:", node)
    for neighbor in graph[node]:
        dfs(neighbor)

dfs("A")
