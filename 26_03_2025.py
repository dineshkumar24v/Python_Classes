'''iii. Write a program to classify a character entered by the user as a vowel, consonant, or neither.'''
# vowels characters or neither

char = input('enter a single character').lower()
if len(char) == 1:
   if char.isalpha():
      if char in ['a', 'e', 'i', 'o', 'u']:
         print('vowels')
      else:
         print('consonants')
   else:
      print('Special characters or non alphabets')
else:
   print('Invalid input length greater than 1')



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


'''Homework Questions'''

'''1. sum of digits'''
num=54312
sum=0
while num > 0:
  rem = num % 10 
  sum=rem+sum      
  num = num // 10  

print(sum)    # 15

'''2. count the digits'''
num=54312
count=0
while num > 0:
  rem = num % 10 
  count+=1      
  num = num // 10

print(count)   # 5


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


