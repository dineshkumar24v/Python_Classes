''' return '''


''' write a function to check whether a number is prime or not '''
# def check_prime(input_num):
#   if input_num <= 1:
#     return False
  
#   for i in range(2, num):
#     if input_num % i == 0:
#       return False
#   return True



''' Arbitary Arguments: in this we have only values '''
# Arbitary ----means random
# here we get values in tuple form...







# *args = arbitary arguments
# def sum(a, b, *c):
#   sum = a + b
#   for i in c:
#     sum += i
#   return sum

# print(sum(4,3,2,1,5,6,6,6,7,8,9))  # 57


# def sum (*args, a, b, c):
#   print(args)   # (1, 5, 6, 6, 7, 8, 9)
#   print(a,b,c)  # 1 2 3

# print(sum(1, 5, 6,6,7,8,9,a=1,b=2, c=3))  # none


# now add only even numbers from an  *args

# def even_sum(*args):
#   sum=0
#   for i in args:
#     if i % 2 == 0:
#       print(i)
#       sum += i
#   return sum
# print(even_sum(1,2,3,4,5,6,7,8,9,10))


''' Keyword arbitary arguments: in this we have both keys and values '''

# NOTE: so to get even the keys we of arbitary args we need to use ** double star
# in this we get output in dictionary form 

# def operation(num1, num2, **c):
#     print(c)  # {'server': 'localhost', 'port': '3308', 'password': '123456', 'location': 'India'}  

# operation(2, 3, server='localhost', port='3308', password='123456', location='India')

# NOTE: so to get even the keys  of arbitary args we need to use ** double star...

def operation(num1, num2, **c):
    print(num1)   
    print(num2)
    for i, j in c.items():
        print(1, j)   

operation(2, 3, server='localhost', port='3308', password='123456', location='India')
# output: 
# 2
# 3
# 1 localhost
# 1 3308
# 1 123456
# 1 India


