# Python print() Function
# The print() function prints the specified message to the screen, or other standard output device.
print('dinesh')   # dinesh
print('dinesh', 'sunny', 'bunny')   # dinesh sunny bunny
# By using a separator
print('dinesh', 'sunny', 'bunny', sep='--')   # dinesh--sunny--bunny

# Variables
int1=29
print(int1)  # 29
print(type(int1))   # <class 'int'>

str1='dinesh'
print(str1) # dinesh
print(type(str1))   # <class 'str'>

flt1=48.384
print(flt1) # 48.384
print(type(flt1))  # <class 'float'>


# Operators
num1=7
num2=3
print(num1+num2)  # 10
print(type(num1+num2))  # <class 'int'>

print(num1-num2)  # 4
print(type(num1-num2))  # <class 'int'>

print(num1*num2)  # 21
print(type(num1*num2))  # <class 'int'>

print(num1/num2)  # 2.3333333333333335
print(type(num1/num2))  # <class 'float'>

print(num1//num2)  # 2  # it is called floor division
print(type(num1//num2))  # <class 'int'>

print(num1**num2)  # 343
print(type(num1**num2))  # <class 'int'>


# Strings
str2='dinesh'
str3='kumar'
# print(str2*str3)   # TypeError: can't multiply sequence by non-int of type 'str'
# print(str2/str3)   # TypeError: unsupported operand type(s) for /: 'str' and 'str'
print(str2+str3)     # dineshkumar
print(str2*6)        # dineshdineshdineshdineshdineshdinesh


# Indexing ---- starts from 0(Zero)
str3='sun rises in the East'
print(str3[0])  # s
print(str3[9])  # space
print(str3[7])  # e

print(len(str3))    # 21

# print(str1[25])    # IndexError: string index out of range

# Negative Indexing  ------ starts form -1
print(str3[-21])  # s ---- here we get first letter
print(str3[-1])   # t ---- here we get last letter


# Slicing
print(str3[0 : 9])    # sun rises
print(str3[3 : 12])   #  rises in
print(str3[ : 7])     # sun ris
print(str3[5 : ])     # ises in the East


print(str3[-4 : ])            # East
print(str3[ : -4])            # sun rises in the 
print(str3[-4 : -12: -1])     # E eht ni


# skip 

# skips every alternate number if 2
str4='abcdefghijklmnopqrstuvwxyz'
print(str4[0:26:2])    # acegikmoqsuwy

str5='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(str5[0:26:2])    # ACEGIKMOQSUWY

str6='0123456789'
print(str6[0:26:2])    # 02468
print(str6[ : :2])     # 02468
print(str6[ : : ])     # 0123456789
print(type(str6))      # <class 'str'>


# COMPLEX NUMBERS

comp1=9 + 10j
comp2=6 + 12j

print(comp1+comp2)       # Addition: (9+10j) + (6+12j) = (15+22j)
print(comp1-comp2)       # Subtraction: (9+10j) - (6+12j) = (3-2j)
print(comp1*comp2)       # Multiplication: (9+10j) * (6+12j) = (54 + 108j + 60j + 120j^2) = -42 + 174j (Note that 𝑗2=−1)
print(comp1/comp2)       # (0.9666666666666667-0.26666666666666666j)  Division: The division of two complex numbers results in another complex number.

# print(comp1//comp2)      # Floor Division: This operation is not supported for complex numbers.
print(comp1**comp2)      # (23.024080878228506-253.56260692198006j)  Exponentiation: This operation is complex and results in a very long complex number.




