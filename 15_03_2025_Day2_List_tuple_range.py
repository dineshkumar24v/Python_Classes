# if we use [] that means it is a list in python 
#  list = []    #This creates an empty list in Python.
# A list is one of Python’s built-in data structures used to store multiple items in one variable.

'''list = [] list is hetrogeneous not homogeneous --- i.e., it can have all data types'''
# Lists are heterogeneous, not homogeneous

# Heterogeneous means the list can contain different types of data at the same time.

# Unlike some programming languages (like Java arrays), Python lists do not require all elements to be of the same type.
# So a list can hold: integers, floats, strings, booleans, other lists, objects, even a mix of all these
# Note: here When we say a Python list can contain “other lists”, it means:

# ✅ A list can store another list as an element 

# Eg:  my_list = [10, "hello", [1, 2, 3]]  Here: 10 → integer, "hello" → string, [1, 2, 3] → another list inside the main list 

# So "other lists" simply means: A list can contain sub-lists (lists inside lists).


# Python lists are heterogeneous, meaning:
# They can store multiple data types in one list 
# They are dynamic, so their size and contents can change
# They allow adding, removing, or modifying items freely

# Note: Homogeneous data structures (like arrays in some languages) require all elements to be of the same type, while heterogeneous structures (like Python lists) allow for a mix of different types.


list1 = [2,5.4, True, 'False', 2+3j, [6,7,9]]
# indexing
print(list1[0])     # 2
print(len(list1))   # 6
# print(list1[0])

#----> Here’s a clear explanation of how to access elements inside nested lists, with examples:

# ✅ Accessing Elements in Nested Lists

# Given a list inside another list:
# my_list = [10, "hello", [1, 2, 3, 4]]

# 1️⃣ Access the inner list
# print(my_list[2])
# Output: [1, 2, 3, 4]

# 2️⃣ Access an element inside the inner list

# Use two indices:
# First index → position of the inner list
# Second index → position inside that inner list

# Example: print(my_list[2][1])
# Output:2
# Explanation:
# my_list[2] → [1, 2, 3, 4]
# my_list[2][1] → element at index 1 of that list → 2

# ✅ Example with a 2D list (matrix)
# matrix = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]
# Accessing elements:
# print(matrix[0][1])   # 20
# print(matrix[1][2])   # 60
# print(matrix[2][0])   # 70

# practice Q :
# Nested List Diagram
# Consider this list:
# data = [10, 20, ["a", "b", "c"], [5, [100, 200], 9]] 



#slicing  --> means to extract a portion of the list
print(list1[1:4])   # [5.4, True, 'False']
print(list1[ :9])   # [2, 5.4, True, 'False', (2+3j), [6, 7, 9]]  # no index out of bound error

# Negative Indexing  ----- starts form -1 // syntax : list1[ -start : -stop : -step]
print(list1[-1 : -4 : -1])   # [[6, 7, 9], (2+3j), 'False']  # here -1 is last index, -4 is 4th last index(excluded), -1 is step (reverse direction)
print(list1[-3: -1])         # ['False', (2+3j)]

# Skiping  ---- means to jump elements while slicing
print(list1[ : : 2])        # [2, True, (2+3j)]   # it skips the 1 element


# we can create list inside list
# accessing list inside another list
temp = list1[5]  # here temp is a list which is inside list1
print(temp)       # [6, 7, 9]
print(temp[1])   # 7

print(list1[5][0])  # 6 
print(list1[5][1])  # 7

# Modifying Lists --- lists are mutable that is we can change the values
# append, extend, insert --- are methods to add elements to a list

# append --- adds value at last place // it adds only single value at last place // directly pass the value to be added
list1.append(55) # append= adds at last place  # extend,  insert # 
print(list1)     # [2, 5.4, True, 'False', (2+3j), [6, 7, 9], 55]

# extend --- it adds multiple values at last place 
list1.extend([88, 99, 'hello']) # here it adds multiple values at last place
print(list1)    # [2, 5.4, True, 'False', (2+3j), [6, 7, 9], 55, 88, 99, 'hello']

# insert --- it adds value at specified index // syntax : list1.insert(index, value)
list1.insert(0, 32) # here it inserts value at 0th index
print(list1)        # [32, 2, 5.4, True, 'False', (2+3j), [6, 7, 9], 55]
list1.insert(1, 36) # here it inserts value at 1st index
print(list1)        # [32, 36, 2, 5.4, True, 'False', (2+3j), [6, 7, 9], 55] 



'''Tuple = In Python, a tuple is an immutable, ordered collection of elements, similar to a list, but its values cannot be changed after creation'''
# tuple --- is immutable that is its value cannot be changed
# if we use parenthesis() that means it is a tuple



tup1 = (2,3, 'True', True, "mango", 12)

#slicing ---> means to extract a portion of the tuple
print(tup1[1: 4])  # (3, 'True', True)
print(tup1[ : 3])  # (2, 3, 'True')

# Negative Indexing 
print(tup1[-1 : -3: -1])  # (12, 'mango') # here -1 is last index, -3 is 3rd last index(excluded), -1 is step (reverse direction)
print(tup1[-3 : -1])      # (True, 'mango') # here -3 is 3rd last index, -1 is last index(excluded)

# reversing a tuple 
print(tup1[ : : -1])      # (12, 'mango', True, 'True', 3, 2)

# Skiping Elements / Jumping
# syntax : tup1[ start : stop : step] 
print(tup1[ 0: 6: 2])       # (2, 'True', 12)   # it skips 1 indexes # here 2 means skip 1 index or if 1 is given it means no skip or 3 means skip 2 indexes
print(tup1[ 0: 6: 3])       # (2, True)    # it skips 2 indexes
print(tup1[ : : 2])         # (2, 'True', 12)   # it skips 1 indexes
print(tup1[ -1: -6: -2])      # (12, True, 3)  # # it skips 1 indexes
print(tup1[ -1: -6: -3])      # (12, 'True')   # it skips 2 indexes
print(tup1[ : : 2])           # (2, 'True', 'mango')   # it skips 1 indexes


# tup1[0] = 2.5      #  TypeError: 'tuple' object does not support item assignment  ----- not possible bec Tuple is immutable
# tup1[1]='fruits'     # TypeError: 'tuple' object does not support item assignment



# In tuple item assignment is not possible, but re-assignment is possible.
tup1 = (2,3, 'True', True, "mango", 12)
tup1= (12, 'hello', 220, 'hi')     # here you can see that re-assignment is possible
print(tup1)    # (12, 'hello', 220, 'hi')


# When to use List vs Tuple?
# Use a list when you need a mutable, ordered collection of items that may change over time.
# Use a tuple when you need an immutable, ordered collection of items that should not change.
# we use tuple where we dont want any changes where data integrity is important
# comparatively tuple is faster than list ---bec of immutability
# i.e., where we cannot tamper it 
# eg: days of week, months of year etc.


# tup1 = (2,)  # single element tuple should have a comma at end otherwise it will be considered as int
# print(type(tup1))   # <class 'tuple'>     
# print(tup1)
# Explanation:
# In Python, (2) is just the integer 2 in parentheses. To create a single-element tuple, you need a comma: (2,).


# ✅ Tuples in Python

# A tuple is an ordered collection of items, like a list, but immutable (cannot be changed after creation).
# Syntax:
# tup = (item1, item2, item3, ...)

# # ✅ Single-element tuple

# If you want a tuple with only one element, you must add a trailing comma.

# Example:

# tup1 = (2,)  # ✅ single-element tuple

# If you forget the comma:

# tup2 = (2)   # ❌ Not a tuple!

# Python interprets (2) as parentheses around an expression, not as a tuple.

# Why the comma?

# The comma tells Python: “This is a tuple, even if there’s only one item.”

# Parentheses alone can be just for grouping expressions, so Python needs the comma to know it’s a tuple.

# ✅ Examples
# tup1 = (2,)
# print(type(tup1))  # <class 'tuple'>

# tup2 = (2) # here it is considered as int because no comma is given
# print(type(tup2))  # <class 'int'> 

# You can also see this works for strings or other types:

# single_str_tuple = ("hello",)
# print(type(single_str_tuple))  # <class 'tuple'>

# 📌 Rule of thumb:
# Always use a comma for a single-element tuple, parentheses alone are not enough.

# String ? -----------> strings in python are immutable
str1 = "Happy new year"
# str1[4] = 'b'   # TypeError: 'str' object does not support item assignment  --- but it allows re-assignment




'''range ---range is used to generate values based on the given range based on upper bound & lower bound'''

# In Python, range(start, stop) generates numbers from start up to (but not including) stop, increasing by +1 by default.
#  syntax : range(lower_bound, upper_bound, step)
# where lower_bound is inclusive and upper_bound is exclusive
r1 = range(1, 10)  # here 1 is lower bound (inclusive) , 10 is upper bound (exclusive)
print(type(r1))       # <class 'range'>
print(r1)             # here it will print range(1, 10)  ---------------> it will not print the values  because range is not a list or tuple 

#so we convert it to either list or tuple to see the values 

print(list(r1))                     # [1, 2, 3, 4, 5, 6, 7, 8, 9] here it prints values from 1 to 9 because 10 is excluded 
print(tuple(r1))                    # (1, 2, 3, 4, 5, 6, 7, 8, 9) 

print(list(range(-5, 22)))         # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

print(list(range(35, 22)))         # []  # because here lower bound is greater than upper bound so it will give empty list 

# Why is the result an empty list []?

# You are telling Python to start at 35 and count upwards (because the default step is +1) until it reaches 22.

# But 35 is already greater than 22, so Python cannot take even a single step forward.

# Since it can't generate any numbers, the result is an empty sequence → [].

# Visualized:
# Start: 35
# Stop: 22
# Step: +1
# Since 35 < 22 is false, the range produces 0 values.
# How to generate a decreasing range instead:
# If you want numbers from 35 down to 23, you must give a negative step:

print(list(range(35, 22, -1)))      # [35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23]

print(list(range(35, 22, -2)))     # [35, 33, 31, 29, 27, 25, 23]  # it skips every alternate Number





