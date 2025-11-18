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


'''3. digit multiple of 3'''
num=54312
# Input number
num = 54312

for digit in str(num): 
    if int(digit) % 3 == 0:  
        print('f{digit} is divisible by 3')


