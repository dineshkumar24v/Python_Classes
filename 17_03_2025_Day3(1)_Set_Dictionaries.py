""" Sets and Dictionaries in Python """
# --------------------------- SETS ------------------------------
# SET = set is a collection of finite unique elements
# In Python, sets are defined using curly braces {} or the set() function.
# set is hetrogeneous, which has unique elements(i.e., duplication is not allowed ) and it is unordered(i.e., it dont print set values as given which is why INDEXING is not possible in set)

s1={1,2,3,4,5,6,7,8,9}
print(type(s1))    # <class 'set'>
print(s1)   # {1, 2, 3, 4, 5, 6, 7, 8, 9}  

# no duplications are allowed
s1={1,2,3,4,5,6,7,8,9,1,2,3,4}
print(s1)    # {1, 2, 3, 4, 5, 6, 7, 8, 9}  

# ✅ 1. Sets are Mutable
# You can add or remove elements from a set.

s = {1, 2, 3}
s.add(4)
print(s)   # {1, 2, 3, 4}

s.remove(2)
print(s)   # {1, 3, 4}

# ✅ 2. Set Elements Must Be Immutable
# You can only store immutable objects inside a set.

# ✔ Allowed: numbers, strings, tuples
# ❌ Not allowed: lists, dictionaries

s = {1, "hello", (1,2)}
# s = {[1,2], 3} ❌ TypeError (list is mutable)

# ✅ 3. No Indexing or Slicing

# Since sets are unordered, you cannot access elements by index.
s = {10, 20, 30}
# print(s[0])  ❌ TypeError
# print(s[1:3])  ❌ TypeError

# When we say “sets are unordered” in Python, it means:
# ✅ 1. The elements in a set do NOT have a fixed position

# Unlike lists or tuples, sets do not store elements in a specific order.

# Example:

s = {10, 20, 30, 40}
print(s)

# Output may be: {40, 10, 20, 30}

# or sometimes: {10, 20, 30, 40}

# The order can change every time you run the program.

# ✅ 2. You cannot access elements using an index

# Since sets have no fixed position, you cannot do this:

s = {1, 2, 3}
print(s[0])     # ❌ ERROR

# Because s[0] does not exist — there is no position 0 in a set.

# ✅ 3. Python arranges set elements internally for fast lookup

# Sets use hashing internally.
# So Python rearranges elements based on hash values — not based on the order you entered them.

# ✅ 4. Order may change when you add or remove elements

# Example:
s = {1, 2, 3}
s.add(4)
print(s)

# Output might be: {1, 2, 3, 4}
# or sometimes: {4, 1, 2, 3}

# 🎯 In simple words:
# Unordered = positions don't exist + order is not guaranteed + indexing not possible.


# ✅ 4. Supports Mathematical Set Operations

# Python sets allow operations like:

# 🔸 Union
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)       # {1, 2, 3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}

# 🔸 Intersection
print(a & b)             # {3}
print(a.intersection(b)) # {3}

# 🔸 Difference
print(a - b)            # {1, 2}
print(a.difference(b))  # {1, 2}

# 🔸 Symmetric Difference
print(a ^ b)                     # {1, 2, 4, 5}
print(a.symmetric_difference(b)) # {1, 2, 4, 5}

# ✅ 5. Duplicates are Automatically Removed

# Useful for removing duplicates from a list:

lst = [1,2,3,2,1,4]
print(set(lst))   # {1, 2, 3, 4}

# ✅ 6. Faster Membership Testing

# Checking if an element exists in a set is much faster than in a list (O(1) vs O(n)).

s = {1,2,3,4,5}
print(3 in s)   # True

# ✅ 7. Empty Set Must Be Created Using set()

# Using {} creates an empty dictionary, not a set.

s = {}       # this is a dict
print(type(s))   # <class 'dict'>

s = set()    # correct empty set
print(type(s))   # <class 'set'>

# ✅ 8. Set Comprehensions Are Supported
s = {x*x for x in range(5)}
print(s)   # {0, 1, 4, 9, 16}

# ✅ 9. Discard vs Remove

# discard() does not raise an error if element is missing; remove() does.
# discard() is safer to use when unsure if element exists. meanwhile remove() is strict and raises error if element is not found. so use remove() when u want to ensure element is present before deletion. and use discard() when u want to avoid errors during deletion.

s = {1,2,3}
s.discard(10)   # No error
# s.remove(10)  # ❌ KeyError

# ✅ 10. Frozen Set (Immutable Set)
#  we use frozenset() to create an immutable set. once created, its elements cannot be changed, added, or removed.
# If you need an immutable set, use frozenset():

fs = frozenset([1,2,3])
print(type(fs))  # <class 'frozenset'>


# -------------------------- DICTIONARIES ---------------------------
#  dictionaries --- it is a collection of key value pairs and is mutable also 
#  
# dict1 = {1:'harish', 2:'suresh', 3:'Ganesh', 4:'prakash'}
# print(dict1)
# print(dict1[2])     # suresh

# db_values = {'db_name': 'localhost/3000', 'db_pass':'secret', 'timeout':30}

# ✅ Python Dictionary Basics

# A dictionary in Python is a collection of key–value pairs.
# It is mutable, ordered (Python 3.7+), and does not allow duplicate keys.

# ⭐ 1. Dictionary Syntax
# dict1 = {key: value}
# Example:

dict1 = {1: 'harish', 2: 'suresh', 3: 'Ganesh'}

# ⭐ 2. Keys Must Be Unique
# If you repeat a key, the last value overwrites the previous one.

d = {1: 'A', 1: 'B'}
print(d)   # {1: 'B'}

# ⭐ 3. Keys Must Be Immutable

# Allowed as keys:
# ✔ int, float
# ✔ string
# ✔ tuple

# Not allowed:
# ❌ list
# ❌ dictionary

# tuple as key is allowed
d = { (1,2): "pair" }   # valid 

# ⭐ 4. Dictionary is Mutable
# You can add, update, or delete items.

# Add a new key-value pair
dict1[4] = "prakash"

# Update a value
dict1[2] = "SURESH"

# Delete a key 
del dict1[3] # removes key 3

# ⭐ 5. Accessing Values
# You access values using keys, not indexes.

print(dict1[2])   # suresh


# Use .get() to avoid errors: missing keys return None instead of KeyError
print(dict1.get(10))     # None (no error)

# ⭐ 6. Dictionary is Ordered (Python 3.7+) it was unordered in earlier versions
# The order in which you insert key-value pairs is preserved. not like sets where order is not preserved.

d = {"a": 1, "b": 2, "c": 3}
print(d)   # same order

# ⭐ 7. No Duplicate Keys, But Duplicate Values Allowed
d = {"a": 10, "b": 20, "c": 10}
# Value 10 appears twice (allowed)

# ⭐ 8. Useful Dictionary Methods
# .keys()
print(d.keys())   # dict_keys(['a', 'b', 'c'])

# .values()
print(d.values()) # dict_values([1, 2, 3])

# .items()
# Returns key–value pairs.

print(d.items())  # dict_items([('a',1), ('b',2), ('c',3)])

# .pop(key)
d.pop("b") # removes key 'b'

# .update()
d.update({"d": 4}) # adds new key 'd'

# ⭐ 9. Looping Through a Dictionary
# Loop through keys
for k in d:
    print(k)

# Loop through values
for v in d.values():
    print(v)

# Loop through key–value pairs
for k, v in d.items():
    print(k, v)

# ⭐ 10. Nested Dictionaries (Dictionary inside Dictionary)
student = {
    "name": "Harish",
    "scores": {
        "math": 90,
        "science": 88
    }
}

print(student["scores"]["math"])   # 90

# ⭐ 11. Example: Realistic Dictionary
db_values = {
    'db_name': 'localhost/3000',
    'db_pass': 'secret',
    'timeout': 30
}

# ⭐ 12. Main Advantages of Dictionary

# Fast data lookup (O(1) Access)

# Easy to store structured data

# Key-value storage makes programs readable

# 🎯 Summary (Most Important Points)
# Property	Dictionary
# Ordered	✔ Yes
# Mutable	✔ Yes
# Keys Unique	✔ Yes
# Key Type	Must be immutable
# Value Type	Any
# Access	By key
# Syntax	{key: value}

