
'''LIST'''
#sum list using for loop
# list1 = [2, -5, 77, 82, -30]

# sum = 0
# for i in list1:
#   # print(i)  # here we get values so we can sum them
#   sum += i

# print(sum)

# sum list using indexing
# list1 = [2, -5, 77, 82, -30]

# sum = 0
# for i in range(0, len(list1)):
#   print(i)
#   sum += list[i]

# print(sum)

# print only the even numbers of the list
# list1 = [2, -5, 77, 82, -30]

# for i in list1:
#  if i%2==0:
#    print(i)

# print only the numbers of even indexes in the list
# list1 = [2, -5, 77, 82, -30]

# for i in range(0, len(list1)):
#   if i % 2 == 0:
#     print(list1[i])

# find the maximum element in the list ?
# list1 = [2, -5, 77, 82, -30]

# print(max(list1))  # 82

# but do with out max Method
# list1 = [-111, -2, -5, -77, -82, -30, -999]

# max = list1[0]
# for i in list1:
#   if max<i:
#     max = i

# print(max)

# print max and min value of a list 
# list1 = [-111, -2, -5, -77, -82, -30, -999]

# max = list1[0]
# min = list1[0]

# for i in list1:
#   if i > max:
#     max = i
#   if i < min:
#     min = i

# print(max,min)


# it is an in-built function where 
max_el = float('-inf') # it represent the negative lowest infinite
min_el = float('inf') # it represent the positive infinite

# print(max_el)

'''print all prime numbers in a list'''
def prime():
    list1 = [27, 17, 29, 42, 47, 100, 22]
    primes = []  # Collect prime numbers
    for num1 in list1:  # Iterate through the values directly
        count = 0
        for i in range(1, num1 + 1):  # Check divisors
            if num1 % i == 0:
                count += 1
        if count == 2:  # Prime condition
            primes.append(num1)  # Add to list of primes
    return primes

print(prime())

# list1 = [2, -5, 77, 82, -30]
# for i in list1:
#     prime()


''' Amstrong Number'''
# Here's the breakdown: 94 = 6561, 44 = 256, 74 = 2401, 44 = 256, and 6561 + 256 + 2401 + 256 = 9474. 

# An Armstrong number is a positive integer where the sum of the digits raised to the power of the number of digits equals the number itself. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153. 

# More examples
# 370 is an Armstrong number because 3^3 + 7^3 + 0^3 = 370. 
# 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371. 
# 407 is an Armstrong number because 4^3 + 0^3 + 7^3 = 407. 
# 1634 is an Armstrong number because 1^4 + 6^4 + 3^4 + 4^4 = 1634. 
# 8208 is an Armstrong number because 8^4 + 2^4 + 0^4 + 8^4 = 8208

# num1 = 9474
# temp = num1

# sum = 0
# while temp > 0:
#   digit = temp % 10
#   sum += digit ** len(str(num1))
#   temp = temp // 10

# if sum == num1:
#   print("Amstrong number")
# else:
#   print('not an amstrong number')


''' Q: find amstrong numbers of a list'''



# def check_amstrong(num1):
#   # num1 = 9474
#   temp = num1

#   sum = 0
#   while temp > 0:
#     digit = temp % 10
#     sum += digit ** len(str(num1))
#     temp = temp // 10

#   if sum == num1:
#     # print("Amstrong number")
#     return sum
#   # else:
#   #   # print('not an amstrong number')
#   #   return "Not"


# list2 = [153, 9774, 8787, 32, 370]
# for i in list2:
#   result = check_amstrong(i)
#   if result != None:
#     print( i)
    

  




