
'''4. CONDITIONAL OPERATORS / LOGICAL OPERATORS : and , or , not '''

print(True and True)  # True
print(True and False)  # False
print(True or False)   # True
print(False and True)  # False
print(False and False)  # False


print(not (True and False))  # ans False but has ! so ans True


print('from here')
print(True or (True and (True and (False and True))))  # True

print(True and (True and (True and (False and True))))  # False

# lets see on numbers:
print(2 and 3)
print(0 and 2)
print('' and 'str')
print([] and [1])


'''Truthy and Falsy values : --- if we convert a value into boolean and if it returns True than it is a Truthy value or else it is a Falsy value'''


print('boolean values')
print(bool(2))  # True
print(bool(-2))  # True
print(bool(0))  # False
print(bool(''))  # False
print(bool('string'))  # True
print(bool())    # False
print(bool([1]))    # True
print(bool([]))    # False

'''so Truthy values are: 2, 3, 'str', [1]'''

'''Falsy Value : 0, '', [] '''

# any number expect 0 is a truthy value
# any string except empty string is a truthy value
# any list except empty list is a truthy value

print('here look')
print( 2 or 3)  # 2
print('' or 5)  # 5
print(bool(None))  # False
print(None or 10)  # 10


'''Bit wise Operators : &, |, ^, >>, <<, ~  '''

# to find the binary value of a number convert num to binary format
# eg:
num1 = 17
print(bin(num1))  # 0b10001

# coverting binary num to an integer number
num1 = 0b10001
print(int(num1))  # 17

# we say it bitwise bec it is comparing every bit


'''bitwise and &'''
print(bin(5))  # 0b101
print(bin(8))  # 0b1000
print(5 & 8)  # 0


print(bin(11))  # 0b1011
print(bin(14))  # 0b1110
print(11 & 14)  # 10

'''bitwise or |'''
print(5 | 8)  # 13
print(bin(13))  # 0b1101

print(11 | 14)  # 15
print(bin(15))  # 0b1111

'''bitwise xor  ^ '''
print(11 ^ 14)   # 5

'''bitwise left swift << '''
# means shifting bits to the left
print(5 << 1)  # 10
print(11 << 1) # 22 
print(13 << 1) # 26
# here you can see that shifting a number by 1 to the left is giving the output as 2 times of the number














