

# while True:
#   temp=temp+1
#   if check_prime(temp):
#     right_prime = temp
#     break

# print(right_prime)

# #Left prime
# temp2 = num1
# left_prime = 'empty'
# while temp2 > 1:
#   temp2 -= 1
#   if check_prime(temp2):
#     left_prime = temp2
#     break

# print(left_prime)

# if left_prime == 'empty':
#   print('Nearest prime is ', right_prime)

# elif num1 -left_prime == right_prime - num1:
#   print(left_prime, right_prime)
# elif num1 -left_prime < right_prime - num1:
#   print(left_prime)
# else:
#   print(right_prime)


'''  RECURSION:   '''
  # A function calling itself is called Recursion....
  #  it will decrease the code complexity...
  # we write it to solve the recursive type of code...

  # but not possible all the time 

  # we use recursion where we try to dive the problem into smaller chunks of problem


  # we try to solve the sub-parts where we automatically get the output of a bigger one...

  # base conditions: are known values ---> here we write the known condition...

# RECURSION TREE: is nothing but which shows how the recursion function executes


''' recursion exapmle for finding a FACTORIAL of a number'''
# def fact(input_num):
#   if(input_num == 1):
#     return 1
#   print(input_num)
#   return input_num * fact(input_num - 1)

# print(fact(5))  



''' printing numbers using recursive function'''
# def print_nums(input_num):
#   if input_num == 0:
#     return
  
#   print_nums(input_num - 1)
#   print(input_num)

# print_nums(7)


'''sum of digits of a number  54321'''

def sum_digit(input_num):
  if input_num==0 :
    return 0
  
  return input_num % 10 + sum_digit(input_num//10)

num1 = 54321
print(sum_digit(num1))


def expo(input_num):
  if input_num==0:
    return 1
  
  return input_num ** input_num-1

print()