
''' NUMBER QUESTIONS : '''
'''5.	A bank rewards its customers who have an account number that is a 'Perfect Number.' A perfect number is a number whose sum of divisors (excluding itself) equals the number itself. Write a program to check whether a given account number is a perfect number. '''
# Examples of perfect numbers 6, 28, 496, and 8128

# sum=0
# input_num=int(input('enter any num '))
# for i in range(1, input_num):
#   if input_num % i == 0:
#     sum += i
# if sum==input_num:
#   print('perfect number')
# else:
#   print('not a perfect number')


''' print prime numbers upto a given range ? '''

num=100
for i in range(1, num+1):
  count = 0
  for j in range(1, i+1):
    if i % j ==0:
      count += 1
  if count==2:
     print(i)

'''6Q. write a program to find LCM of two numbers'''
# The least common multiple (L.C.M.) of two numbers is the smallest positive integer that is perfectly divisible by the two given numbers.

# print('enter nums to find LCM of two numbers')
# num1=int(input('enter num1 '))
# num2=int(input('enter num2 '))

# if num1>num2:
#   greater = num1
# else: 
#   greater = num2

# while(True):
#   if greater % num1 == 0 and greater%num2==0:
#     lcm = greater
#     break
#   greater += 1

# print('lcm of ',num1,'&',num2, 'is', lcm )

# NOTE: The program goes through each natural number one by one. This can take a long time if the numbers that are input are quite large or prime numbers themselves. 

# so lets see how to calculate LCM using GCD
# FORMULE : product of two numbers = LCM * GCD




'''HCF or GCD of two numbers: '''
# The highest common factor (H.C.F) or greatest common divisor (G.C.D) of two numbers is the largest positive integer that perfectly divides the two given numbers.

# print('enter nums to find HCF of two numbers')
# num1=int(input('enter num1: '))
# num2=int(input('enter num2: '))

# if num1<num2:
#   smaller = num1
# else : 
#   smaller = num2

# for i in range(1, smaller+1):
#   if num1 % i == 0 and num2 % i == 0 :
#     hcf = i
  
# print('HCF of ',num1,'and',num2,'is', hcf)




