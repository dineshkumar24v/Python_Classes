# list = [] list is hetrogeneous not homogeneous
# if we use [] that means it is a list in python


list1 = [2,5.4, True, 'False', 2+3j, [6,7,9]]
# indexing
print(list1[0])     # 2
print(len(list1))   # 6
# print(list1[0])

#slicing
print(list1[1:4])   # [5.4, True, 'False']
print(list1[ :9])   # [2, 5.4, True, 'False', (2+3j), [6, 7, 9]]  # no index out of bound error

# Negative Indexing
print(list1[-1 : -4 : -1])   # [[6, 7, 9], (2+3j), 'False']
print(list1[-3: -1])         # ['False', (2+3j)]

# Skiping
print(list1[ : : 2])        # [2, True, (2+3j)]   # it skips the 1 element


# we can create list inside list
# accessing list inside another list
temp = list1[5]
print(temp[1])   # 7

print(list1[5][0])  # 6
print(list1[5][1])  # 7

list1.append(55) # append= adds at last place  # extend,  insert
print(list1)     # [2, 5.4, True, 'False', (2+3j), [6, 7, 9], 55]

list1.insert(0, 32) # here it inserts value at 0th index
print(list1)        # [32, 2, 5.4, True, 'False', (2+3j), [6, 7, 9], 55]



# Tuple = In Python, a tuple is an immutable, ordered collection of elements, similar to a list, but its values cannot be changed after creation
# tuple --- is immutable that is its value cannot be changed

# if we use parenthesis() that means it is a tuple

tup1 = (2,3, 'True', True, "mango", 12)

#slicing
print(tup1[1: 4])  # (3, 'True', True)
print(tup1[ : 3])  # (2, 3, 'True')

# Negative Indexing
print(tup1[-1 : -3: -1])  # (12, 'mango')
print(tup1[-3 : -1])      # (True, 'mango') 

# reversing a tuple 
print(tup1[ : : -1])      # (12, 'mango', True, 'True', 3, 2)

# Skiping Elements / Jumping
print(tup1[ -1: -6: -2])      # (12, True, 3)  # # it skips 1 indexes
print(tup1[ -1: -6: -3])      # (12, 'True')   # it skips 2 indexes
print(tup1[ : : 2])           # (2, 'True', 'mango')   # it skips 1 indexes


# tup1[0] = 2.5      #  TypeError: 'tuple' object does not support item assignment  ----- not possible bec Tuple is immutable
# tup1[1]='fruits'     # TypeError: 'tuple' object does not support item assignment



# In tuple item assignment is not possible but re-assignment is possible.
tup1 = (2,3, 'True', True, "mango", 12)
tup1= (12, 'hello', 220, 'hi')     # here you can see that re-assignment is possible
print(tup1)    # (12, 'hello', 220, 'hi')


# we use tuple where we dont want any changes where 
# comparatively tuple is faster than list ---bec of immutability
# i.e., we cannot tamper it 


# tup1 = (2,3)
# print(tup1)



# String ? -----------> strings in python are immutable
str1 = "Happy new year"
# str1[4] = 'b'   # TypeError: 'str' object does not support item assignment  --- but it allows re-assignment




# range
r1 = range(1, 10)
print(type(r1))                      # <class 'range'>

print(list(r1))                     # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(-5, 22)))         # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

print(list(range(35, 22)))         # []

print(list(range(35, 22, -1)))      # [35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23]

print(list(range(35, 22, -2)))     # [35, 33, 31, 29, 27, 25, 23]  # it skips every alternate Number





