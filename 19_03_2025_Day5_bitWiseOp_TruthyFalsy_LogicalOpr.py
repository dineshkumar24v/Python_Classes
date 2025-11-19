
''' --- 4. CONDITIONAL OPERATORS / LOGICAL OPERATORS : and , or , not '''

print(True and True)  # True
print(True and False)  # False # here as one value is False so the whole expression is False
print(True or False)   # True # here as one value is True so the whole expression is True
print(False or False)  # False
print(False and True)  # False
print(False and False)  # False

# not operator
print(not True)  # ans False
print(not (True and False))  # ans False but has ! so ans True


print('from here') # more complex examples
print(True or (True and (True and (False and True))))  # True

print(True and (True and (True and (False and True))))  # False

# lets see on numbers:
print(2 and 3) # 3 # here both values are truthy so it returns the last value
print(0 and 2) # 0 # here first value is falsy so it returns the first falsy value
print(2 and 0) # 0 # here second value is falsy so it returns the second falsy value
print(0 and 0) # 0 # here both values are falsy so it returns the first falsy value
print('' and 'str') # '' # here first value is falsy so it returns the first falsy value
print('str' and '') # '' # here second value is falsy so it returns the second falsy value
print('str' and 'hello') # 'hello' # here both values are truthy
print([] and [1]) # [] # here first value is falsy so it returns the first falsy value


'''Truthy and Falsy values : --- if we convert a value into boolean and if it returns True than it is a Truthy value or else it is a Falsy value'''


print('boolean values')
print(bool(2))  # True # so numbers except 0 are truthy values
print(bool(-2))  # True # negative numbers are also truthy
print(bool(0))  # False # 0 is a falsy value
print(bool(''))  # False # empty string is  a falsy value
print(bool('string'))  # True # whereas non emty string is a truthy value 
print(bool())    # False # default value of bool is false
print(bool([1]))    # True # non empty list is a truthy value
print(bool([]))    # False # empty list is a falsy value

'''so Truthy values are: 2, 3, 'str', [1]'''

'''Falsy Value : 0, '', [] '''

# any number expect 0 is a truthy value
# any string except empty string is a truthy value
# any list except empty list is a truthy value

print('here look')
print( 2 or 3)  # 2 # here 2 is a truthy value so it returns 2
print( 0 or 3)  # 3 # here 0 is a falsy value so it returns 3
print( 0 and 3)  # 0 # here 0 is a falsy value so it returns 0
print( 2 and 3)  # 3 # here both values are truthy so it returns the last value
print('str' or '')  # 'str' # here 'str' is a truthy value so it returns 'str'
print('' or 5)  # 5 # here '' is falsy so it returns 5
print(bool(None))  # False # None is a flasy value
print(None or 10)  # 10 # here None is falsy so it returns 10
print(None and 10)  # None # here None is falsy so it returns None


'''--------------------- Bit wise Operators : &, |, ^, >>, <<, ~  '''

# to find the binary value of a number convert num to binary format
# eg:
num1 = 17
print(bin(num1))  # 0b10001

# coverting binary num to an integer number
num1 = 0b10001
print(int(num1))  # 17

# we say it bitwise bec it is comparing every bit


'''bitwise and &''' 
# ✅ 1. Bitwise AND → &
# Rule:
# 1 & 1 = 1
# otherwise = 0

# Example:
# 5 → 0101
# 8 → 1000

#   0101
# & 1000
# ------
#   0000  → decimal 0

print(bin(5))  # 0b101
print(bin(8))  # 0b1000
print(5 & 8)  # 0 


print(bin(11))  # 0b1011
print(bin(14))  # 0b1110
print(11 & 14)  # 10

'''bitwise or |'''
# ✅ 2. Bitwise OR → |
# Rule:
# 1 | 1 = 1  
# 1 | 0 = 1  
# 0 | 1 = 1  
# 0 | 0 = 0

# Example:
# 5 → 0101
# 8 → 1000

#   0101
# | 1000
# ------
#   1101  → decimal 13
print(5 | 8)  # 13
print(bin(13))  # 0b1101

print(11 | 14)  # 15
print(bin(15))  # 0b1111

'''bitwise xor  ^ '''
# ✅ 3. Bitwise XOR → ^
# Rule:
# If bits are SAME → 0  
# If bits are DIFFERENT → 1

# 11 → 1011
# 14 → 1110

#   1011
# ^ 1110
# ------
#   0101 → decimal 5

# ✔ XOR highlights difference between bits.
print(11 ^ 14)   # 5

'''bitwise left swift << '''
# 1️⃣ Left Shift << (Multiply by 2)
# Rule: Shift all bits left, fill 0 on the right. Each shift doubles the number.
# means shifting bits to the left
print(5 << 1)  # 10 # this means 5*2=10
print(11 << 1) # 22 # this means 11*2=22
print(13 << 1) # 26 # this means 13*2=26
# here you can see that shifting a number by 1 to the left is giving the output as 2 times of the number

# ✅ Observation:
# Each shift left multiplies by 2
# n << 1 = n2, n << 2 = n4, etc.


# 🔹 5. Bitwise RIGHT SHIFT → >>
# Meaning:
# Shift all bits to the right
# Drops bits on the right
# Each shift divides the number by 2 (integer division)
# Right Shift >> (Divide by 2)
# Rule: Shift all bits right, drop bits on the right. Each shift halves the number (floor division).

# Example: 
print(12 >> 1) # 6
print(13 >> 2) # 3

# ✅ Observation:
# Each shift right divides by 2 (integer division)
# n >> 1 = n//2, n >> 2 = n//4, etc.


# 🔹 6. Bitwise NOT → ~  (Invert Bits)
# Meaning:
# Flips all bits
# 0 → 1, 1 → 0
# Works as two’s complement for negative numbers
# Bitwise NOT ~ 
# Rule: Flip all bits. In Python, returns - (n+1) because of two’s complement.

# Example:
print(~10) # -11

# ✅ Observation:
# ~n = -(n+1)
# Flips 0→1 and 1→0


# Visual Summary Table
# Operator	Example	Binary Before	Binary After	Decimal Result
# <<	5 << 1	0101	1010	10
# >>	12 >> 2	1100	0011	3
# ~	~5	00000101	11111010	-6












