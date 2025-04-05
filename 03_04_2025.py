'''SCOPES : Accessibility of a variable or an entity is called scope '''
'''here we have only two scopes in python 1. LOCAL 2.GLOBAL'''
# GLOBAL: A variable which is accessed any where after it is declared is called Global Variable
# there is no concept of hoisting in python so a variable cannot be accessed before it is declared
# Eg:
# num = 10
# def check():
#   print(num)


# if 5>2:
#   print(num)

''' LOCAL SCOPE : '''
# def check_local():
#   num2 = 25
#   print(num2)

# check_local()
# print(num2) # cant access a variable which is declared inside a function

'''Lambda functions : these are not void functions---ie., they have return statements '''
# LAMBDA Functions : are Anonymous one line functions...
# mostly we use Lambda functions in Higher order functions -- means 
# lambda function means use lambda

# example_lambda = lambda x : x * 2
# print(example_lambda(5))
# print(example_lambda(10))
# print(example_lambda(13))


# example_lambda = lambda x, y:x + y
# print(example_lambda(2, 7))
# example_lambda = 10
# print(example_lambda(2, 7))

# w

'''higher order functions : are those functions which takes one more function as an argument..... map(),  filter,  reduce'''

''' 1. map()--- generally takes two argumments....
'''
# def dbl(y): # double function
  # return y * 2

# def trp(x):  # triple function
#   return y * 3

# print(list(map(lambda x: x * 4 , [10, 20, 45, 64, 75])))

# print(list(map(lambda x: x * 2 , [11, 23, 50, 66, -7])))


'''filter method :'''

# print(list(filter(lambda x: x%2==0, [11, 23, 50, 66, -7])))

# print(list(filter(lambda x: x> 0 and x<22, [11, 23, 50, 66, -7])))


'''reduce Method:'''
# filter and map are directly accessible but reduce need to be imported to use it bec everything is not accessible....

# we dont use reduce method frequently so we took it and kept it in a module named function tools...

# so we need to import reduce from function tools to import it...
from functools import reduce

print(reduce(lambda x,y: x + y, [11, 23, 50, 66, -7])) #we get sum f list = 143

print(reduce(lambda x,y: x - y, [11, 23, 50, 66, -7])) # we get sub f list = -121

print(reduce(lambda x,y: x * y, [11, 23, 50, 66, -7])) # we get mul f list = -5844300

print(reduce(lambda x,y: x / y, [11, 23, 50, 66, -7])) # we get div f list = -2.0703933747412007e-05  