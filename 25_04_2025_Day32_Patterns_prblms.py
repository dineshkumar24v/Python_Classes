

# i == n-1 => spaces = 0 => 0 == n-i-1 => spaces =n-i-1
# i == n-2 => spaces = 1 => 0 == n-i-2 => spaces-1 = n-i-2 => spaces =
# i == n-3 => spaces = 2

#       * 
#      * * 
#     * * * 
#    * * * * 
#   * * * * * 
#  * * * * * * 
# * * * * * * * 

n = 7
for i in range(n):
  for k in range(n -i - 1):
    print(' ', end= '')
  for j in range(n):
    if i>= j:
      print('*', end=' ')
  print()

print('------------------------')

#       *
#      * *
#     *   *
#    *     *       
#   *       *     
#  *         *   
# * * * * * * *

n = 7
for i in range(n):
  for k in range(n -i - 1):
    print(' ', end= '')

  for j in range(n):
    if i == j or i == n-1 or j == 0:
      print('*', end=' ')
    else:
      print(' ', end = ' ')
  print()

print('------------------------')

# print fibanocci series 
# 0
# 1 1
# 2 3 5
# 8 13 21 34
# 55 89 144 233 377
# 610 987 1597 2584 4181 6765
# 10946 17711 28657 46368 75025 121393 196418       

n=7
num1, num2 = 0,1
for i in range(n):
  for j in range(n):
    if i >= j:
      print(num1, end = ' ')
      num1, num2 = num2, num1 + num2
  print()


print('--------------------')

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

n = 5
for i in range(n):
  for k in range(2*(n-i-1)):
    print(' ', end= '')

  for j in range(2*i+1):
      print('*', end=' ')
  print()

print('------------------------')

#         1
#       2 1 0
#     3 2 1 0 -1
#   4 3 2 1 0 -1 -2
# 5 4 3 2 1 0 -1 -2 -3 

n = 5
for i in range(n):
  start = i+1
  for k in range(2*(n-i-1)):
    print(' ', end= '')

  for j in range(2*i+1):
      print(start, end=' ')
      start-=1
  print() 

print('------------------------')


#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5

n = 5
for i in range(n):
  track1=False
  start = i+1
  for k in range(2*(n-i-1)):
    print(' ', end= '')

  for j in range(2*i+1):
      print(start, end=' ') 
      if start == 1:
        track1 =True

      if track1 == False:
        start = start -1
      else:
        start += 1
  print() 


# Method 2

for i in range(i, i+2):
  str1 = str(i) = ' ' + str1


print(str1)


# OOPS
# Inheritance
# Polymorphism
# Method Overloading
# Method Overriding


class HumanBeing:
  def __init__(self, name, gender, dob):
    self.__name = name
    self.__gender = gender
    self.__dob = dob
    print('Human object created')
  
  def introduce(self):
    print(self.__name, self.dob)

  def get_name(self):
    return self.__name
  

  




# Abstraction




# Swapping

# Method 1
a,b = 10, 20
a, b = b, a


# Method 2
a, b = 10, 20
temp = b
b = aa = temp

# Method 3
a = 10
b = 20
a = a + b
   





