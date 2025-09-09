'''FUNCTIONS:  --- it is a reusable piece of code which can be executed whenever it is called......'''
# we use it to avoid redundancy ie., to avoid repetition of code......
# to decrease space
# to decrease file size ---- so that server load fast bec of small file size
# decrease the number of lines of code
# and even decrease the compilation time  --- bec the compiler already has the function definition so it will predict the output no need to again see the every line of code.....
# function makes our life easy....


'''function definition :'''

def sample_function():
  print('1st function')
  print('hai, from function')
# NOTE: with out calling a function it wont be executed....
# print('hiii')
# sample_function()

# NOTE: we can call the function multiple times
# sample_function()
# sample_function()
# sample_function()
# sample_function()

# function definition and declaration both are same.....

# see its real-time usage:
def calc_volume(rad):  #parameters
  print(4/3 * 3.14 * rad * rad * rad) # function body


# calc_volume(10)  # arguments
# calc_volume(20)  # function calling
# calc_volume(30)  # function calling
# calc_volume(40)  # function calling

def simple_calculator(a,b): # parameters
  print(a+b)
  print(a-b)
  print(a*b)
  if b!=0:
    print(a/b)
  else:
    print('division by zero not possible')

# simple_calculator(10,2) # function calling by arguments 



'''types of arguments:'''
'''1. Positional Arguments :'''
(a,b,c) = (1,2,3)
# here a=1, b=2, c=3
# parameters takes arguments based on positions only


'''2. Default Arguments: '''
def defalt_para(a,b,c='india'):
  print(a)
  print(b)
  print(c)
defalt_para(1,2) # 1 2 india
# so if u dont give any arguemts it take default arguments


'''key word Arguments---- here we clearly say which parameter should take which argument'''

# here we need not necessary to bother about the position of arguments as we pass them while calling  a function so no ambiguity......

defalt_para(b=5, c='nigeria', a=10) # this is called keyword arguments as we are clearly saying which parameter should take which argument so no ambiguity



'''todays question'''
'''print 1st n natural nos using function'''
def Natural_nums(input_num):
  for i in range(1,input_num):
    print(i)

Natural_nums(21)

'''check whether a num is even or odd'''
def check_even_odd(input_num):
  if input_num%2==0:
    print('even')
  else:
    print('odd')

check_even_odd(29)

'''check whether a num is prime number or not'''
def check_prime(num2):
  count = 0
  for i in range(1, num2+1):
    if num2 % i == 0:
      count += 1
  if count == 2:
    print('prime')
  else:
    print('not prime')

check_prime(17)



''' now lets talk about "return keyword" :'''
# if we use print it will print the value in the console thats it but we cant use it again 

# but by using return we can store that value in a variable and re-use that value where ever needed 

def sum(a,b):
  print(a+b)
def sum2(a,b):
  return a-b

sum(2,3)  # 5
sum2(2,3)  # here it will not print output bec we are not printing the output we are just storing the output in return statment

# so to print the return value 1st assign it a variable and store the return value in that variable so that u can print that value

result = sum2(5,2)
print(result)  # 3

# now let us re-use the return

def sum3(a,b):
  return a-b, a+b, a*b

res = sum3(2,5)
print(res)   # (-3, 7, 10)
print(res*3) # (-3, 7, 10, -3, 7, 10, -3, 7, 10)

