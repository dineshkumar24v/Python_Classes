'''write a program to print whethear a number is a palindrome or not'''
# num1 = 9999
# temp = num1

# rev_num = 0
# while temp > 0 :
#   digit = temp % 10
#   rev_num = rev_num * 10 + digit
#   temp = temp // 10

# print(rev_num)

# if num1 == rev_num:
#   print('palindrome')


'''vii. Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a while loop.'''
# # using break
# while True :
#   num1 = int(input('enter a non-negative number '))
#   if num1<0:
#     print('negative number you did not followe d the condition')
#     break 


# # without using break
# num1 = int(input('enter a non-negative number '))
# while num1 >= 0:
#   print(num1)
#   num1 = int(input('enter a non-negative number '))


'''i. Print the first 10 terms of the Fibonacci series using a for loop.'''
# n=20
# num1, num2 = 0 , 1
# print(num1,'\n',num2)
# for i in range(1,n):
#   num3=num1+num2
#   print(num3)
#   num1=num2
#   num2=num3


'''v. Implement a menu-driven program where the user can choose to: 
1. Find the square of a number. 
2. Find the cube of a number. 
3. Exit.'''


'''vi. Implement a basic login system where the user has three attempts to enter the correct password using a loop.'''


# 1 time right
db_username='john'
db_password=12345


input_usename = input('enter usename')
input_password = input('enter password')

if input_usename == db_username  and  db_password == input_password:
  print('login successful')
else:
  print('login failed')

# now giving 3 attempts condition ?

db_username='john'
db_password=12345

rem_attempts = 3

while rem_attempts > 0:

  input_usename = input('enter usename')
  input_password = input('enter password')

  if input_usename == db_username  and  db_password == input_password:
    print('login successful')
    break  # if we dont use break it again asks for username
  else:
    rem_attempts -= 1
    if rem_attempts == 0:
      print('try after 24 hrs')
    else:
      print('login failed', 'you still have', rem_attempts)
  








