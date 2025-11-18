'''2. Loops: 
a. Easy Questions: 

i. Print all numbers from 1 to 100 using a for loop.'''

# for i in range(1,101):
  # print(i)


''' ii. Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)'''
# METHOD 1:
sum=0
for i in range(1,21):
  sum +=i
print(sum)  # 210

# METHOD 2:
n=20

print(n*(n+1)/2)  # 210.0


'''iii. Print all even numbers between 1 and 50 using a while loop.'''

# for i in range(2, 50, 2):
#   print(i)


'''iv. Write a program to display the multiplication table of a given number. First 20'''

# num=int(input('enter any number '))
# for i in range(1,21):
#    print(num, '*',i,'=',num*i )
#    i+=1
   

# num=int(input('enter any number '))
# for i in range(1,num+1):
#   for j in range(1,11):
#     print(i, '*',j,'=',i*j )
    

# print every table upto 20
for i in range(1,11):
  for j in range(1,21):
    print(i,'*',j,'=',i*j)
  print('---------**----------')
  

'''v. Reverse a number using a while loop. 1. Also can we get the sum of all the digits.'''

# num=123456

# while num > 0:
#   rem = num % 10 
#   print(rem)      # 6 5 4 3 2 1
#   num = num // 10

num=123456
rev_num=0

while num > 0:
  rem = num % 10 
  # print(rem)     
  rev_num = rev_num * 10 + rem
  num = num // 10

print(rev_num) 

'''vi. Write a program to count the number of digits in a given number using a while loop.'''

'''count the digits'''
num=54312
count=0
while num > 0:
  rem = num % 10 
  count+=1      
  num = num // 10

print(count)   # 5


''' sum of digits'''
num=54312
sum=0
while num > 0:
  rem = num % 10 
  sum=rem+sum      
  num = num // 10  

print(sum)    # 15


'''3. print only multiple of 3 from that number'''
''' using while loop''' 
num = 654312
while num > 0:
    rem = num % 10  # Extract the last digit
    if rem % 3 == 0:
        print(rem, 'divisible by 3')
    num = num // 10  # Remove the last digit

# output: 
# 3 divisible by 3
# 6 divisible by 3

# === Code Execution Successful ===

'''using for loop'''

num = 54312

for digit in str(num): 
    if int(digit) % 3 == 0:  
        print(digit,' is divisible by 3')


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




                            #  '''b. Medium Questions:'''

'''i. Print the first 10 terms of the Fibonacci series using a for loop.'''
# n=20
# num1, num2 = 0 , 1
# print(num1,'\n',num2)
# for i in range(1,n):
#   num3=num1+num2
#   print(num3)
#   num1=num2
#   num2=num3


'''ii. Check if a given number is a prime number using a for loop.'''
# num=97
# is_prime=True
# for i in range(2,num):
#   if num%i==0 :
#     is_prime=False
#     break
# if is_prime and num>1:
#     print(num,' is prime')
# else:    
#     print(num,' is not prime')

'''iii. Write a program to calculate the factorial of a number using a while loop.'''

# num=5
# fact=1
# i=1
# while i<=num :
#   fact *= i
#   i=i+1
  
# print(fact)

'''iv. Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.'''

# for i in range(1,101):
#   if i%3==0 and i%5==0 :
#     print(i)


'''v. Implement a menu-driven program where the user can choose to: 
1. Find the square of a number. 
2. Find the cube of a number. 
3. Exit. '''



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