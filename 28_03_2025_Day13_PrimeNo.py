

'''prime number question'''

# Prime number = A number having only 2 factors 

# Method 1:

num1=17
count =0
for i in range(1, num1+1):
  if num1 % i == 0:
    # print(i)
    count += 1
if count ==2:
  print('prime')
else:
  print('not prime')  # prime
  
# print('prime number') if count == 2 else print('not  a prime number')


# Method 2:

num1 = 9
spy = False 

for i in range(2, num1):
  if num1 % 1 == 0:
    spy = True
    print('It is not a prime')
    break
if spy == False:
  print('prime number')
else: 
  print('not a prime number')

# Method 3:

num1 = 9
spy = False 

for i in range(2, num1//2+1):   # 2 to 12
  if num1 % 1 == 0:
    spy = True
    print('It is not a prime')
    break
if spy == False:
  print('prime number')
else: 
  print('not a prime number')

# Method 4:  is most efficient as it will have less no of iterations

num1 = 9
spy = False 

for i in range(2, int(num1 ** 0.5)+1):   # 2 to 12
  if num1 % 1 == 0:
    spy = True
    print('It is not a prime')
    break
if spy == False:
  print('prime number')
else: 
  print('not a prime number')




