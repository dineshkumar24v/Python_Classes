""" Strings in detail and Type Conversions in Python"""
#------------------- Why String in Python is immutable? ----------------------

# ✅ Why Strings in Python Are Immutable
# Immutability means:

# Once a string is created, you cannot change its characters.
# Any change creates a new string in a new memory location.

# 🔍 1. Python stores identical strings in the same memory (string interning)

# Example:

str3 = 'suresh'
str4 = 'suresh'
print(id(str3))
print(id(str4)) 


# ✔ Since both strings have the same value, Python stores only one copy internally.
# ✔ Both variables point to the same memory address.

# This is possible because strings are immutable → Python knows they cannot change, so it is safe for both variables to share the same memory.

# 🔥 2. If strings were mutable, this would be dangerous

# Imagine this:

# If str3 and str4 both pointed to the same string in memory and strings were mutable:

str3[0] = 'X'   # (if mutation were allowed)


# Then it would ALSO modify str4, because both share memory.

# This is unacceptable and breaks code safely.

# 👉 To avoid such problems, strings are made immutable.

# 🧠 3. Immutability helps with:
# ✔ memory optimization (string interning)
# ✔ faster performance
# ✔ safe to use as dictionary keys
# ✔ thread-safety

# Because strings cannot change, Python can reuse them safely.

# 🔍 4. Demonstration using id() (memory address)
# Integers are also immutable
str1 = 5
str2 = 5
print(id(str1))  
print(id(str2))


# ✔ Same memory address
# ✔ Same reason → integers are immutable

# Strings behave the same
str3 = 'suresh'
str4 = 'suresh'
print(id(str3))
print(id(str4))


# ✔ Same memory (interning)

# Because neither variable can modify the string.

# 🔍 5. Converting string to integer or float
str1 = '12.5'
print(int(str1))      # ❌ Error
print(float(str1))    # ✔ 12.5

# Why error?

# int() accepts only whole numbers inside a string:

# ✔ '15'
# ✔ '329'

# ❌ '12.5' contains a decimal → not a valid integer literal.

# float() accepts decimal values, so it works.

# 🎯 FINAL SUMMARY (Very Clear Notes)
# Why strings are immutable?
# To prevent accidental changes
# To allow memory optimization (interning)
# To make strings safe as dictionary keys
# For faster performance
# To avoid multiple variables modifying the same string

# How we know they're immutable?
# Because identical strings share the same memory address, meaning Python treats them as constant values.
# id ing means memory address of that particular object in python
str1=5
print(id(str1))   # 140727504865848
str2=5
print(id(str2))   # 140727504865848
# both str1 and str2 point to same memory location since value is same 


str3 = 'suresh'
print(id(str3))    # 1499841976944
str4 = 'suresh'
print(id(str4))    # 1499841976944
# both str3 and str4 point to same memory location since value is same


str1='12.5'
print(int(str1))  # ValueError: invalid literal for int() with base 10: '12.5'
print(float(str1))  # 12.5


# -------------What happens when you try to modify a string? -----------------
# 🚫 Strings are Immutable — You Cannot Change Them

# If you try to modify (change/update/delete) any character inside a string,
# Python will raise an error, because strings cannot be changed after creation.

# 🔥 1. Trying to change a character
s = "hello"
s[0] = "H"

# ❌ Output
# TypeError: 'str' object does not support item assignment

# ✔ Why?
# Python does not allow you to modify any individual character inside a string.

# 🔥 2. Trying to delete a character
s = "hello"
del s[1]

# ❌ Output
# TypeError: 'str' object doesn't support item deletion

# Again → cannot modify the original string.
# 🔥 3. Even slicing doesn’t modify the string
# Slicing creates a new string, leaving the original unchanged.

s = "hello"
new_s = s[:2] + "X" + s[3:]
print(new_s)  # heXlo
print(s)      # hello (unchanged)

# 🔥 4. Any “modification” creates a NEW string

# Example:
s = "hello"
s = s.upper() # creates a new string "HELLO"
print(s)      # HELLO
print(s)      # hello (original string remains unchanged)
# The uppercase version is not applied to the original string.

# Behind the scenes:
# "hello" stays in memory
# upper() creates a new string "HELLO"
# s now points to the new memory --> it no longer points to "hello" means here s is reassigned to new string "HELLO" 
# NOTE: does this means immutable property is violated? 
# NO because original string "hello" is still intact in memory it is not changed or modified only s variable is reassigned to new string "HELLO" 
# but now how to access original string "hello"? 
# we can access it only if we have another variable pointing to it before reassignment otherwise it is lost forever.
# that is why we should not do s = s.upper() directly if we want to keep original string intact we should do like this new_s = s.upper()


# 🔍 5. Proof using id()
s = "hello"
print(id(s))

s = s + " world"
print(id(s))


# Two different id() → proves a new object was created.

# 🔥 6. Why Python does this?

# Because strings are:
# ✔ immutable
# ✔ shared internally (string interning)
# ✔ optimized for speed and memory
# ✔ safe to use as dictionary keys

# ✔ SUMMARY (Very Clear)
# When you try to modify a string:
# You get a TypeError
# Strings cannot be updated, deleted, or changed
# Any modification creates a new string in a new memory location


#------------------------------------------ Type Conversion ----------------------------------
# float ----------- to ----------- int
num1 = 4.5
print(int(num1))    # 4
print(num1)         # 4.5 here num1 is still float it remains unchanged because we didn't change num1 value we just printed int(num1) which converts float to int only for that print statement

# int ----to ------float
num1 = int(num1) # 4
num1 = float(num1) # 4.0
print(num1)         # 4.0

# string ---------- to ---------list
str1= 'string example'
list1 = list(str1)
print(list1)    # ['s', 't', 'r', 'i', 'n', 'g', ' ', 'e', 'x', 'a', 'm', 'p', 'l', 'e']


# Type conversion means changing the data type of a value into another data type.

# In Python, you can convert:
# string → int
# int → float
# float → string
# int → string
# list → set
# tuple → list
# … and many more.

# ✅ Simple Definition
# Type Conversion = Changing one data type to another.

# Example:
x = "25"
y = int(x)     # string → integer
print(y)       # 25

# ⭐ Two Types of Type Conversion
# 1️⃣ Implicit Type Conversion (Automatic)

# Python automatically converts one type to another without your action.

# Example:

a = 10      # int
b = 2.5     # float
c = a + b   # int + float
print(c)    # 12.5


# Python converts int → float automatically.

# 2️⃣ Explicit Type Conversion (Manual)

# You convert data types manually using functions.

# Examples:
# string → int
x = "10"
y = int(x)

# string → float
x = "12.5"
y = float(x)

# int → float
x = 5
y = float(x)    # 5.0

# float → int
x = 12.7
y = int(x)      # 12 (decimal removed)

# number → string
x = 100
y = str(x)      # "100"

# list → set
lst = [1,2,3,1]
s = set(lst)    # removes duplicates

# 🎯 SUMMARY (Very Clear Notes)

# ✔ Type Conversion = Changing data type

# ✔ Two types:
# Implicit (automatic)
# Explicit (manual using functions)
# ✔ Common functions: int(), float(), str(), list(), set(), tuple()


