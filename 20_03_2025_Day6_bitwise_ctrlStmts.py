
'''bitwise left swift << '''
# means shifting bits to the left
print(5 << 1)  # 10 --- 5 * 2
print(11 << 1) # 22 --- 11 * 2
print(13 << 1) # 26 --- 13 * 2

# lets now take negative numbers and see
print(-5 << 1)  # -10
print(-11 << 1) # -22 
print(-13 << 1) # -26

'''bitwise right swift >> '''
# means shifting bits to right
print(5 >> 1)  # 2
print(11 >> 1) # 5 
print(13 >> 1) # 6
# here we can observe that we are getting floor division by 2 values of the number
#  5 // 2  --- 2

# now lets see left shift and right shift by 2
print(5 << 2)  # 20 --- 5 * 4

print(5 >> 2)  # 1   --- 5 // 4

'''bitwise complement ~'''

print(~12)  # -13  # here you can see that one num is added and sign also changed
print(~25)  # -26
print(~-13) # 12
print(~33)  # -34


                   
'''CONTROL STATEMENTS: control statements are the statements which controls the flow of execution of a code '''
'''Different Types are: '''
'''1. CONDITIONAL STATEMENTS: if else , elif'''
# if else , elif 
# python dont have concept of flower brackets it has concept of '''indentation'''
'''1. if else :'''
age = 17 
if age >= 18:
  print('I can vote')
else:
  print('I cannot vote')  

# python is semi-compiled and than interpreted --- i.e., it 1st checks the basic indentation and throws error if wrong andd later act as interpreted language

'''check if a number is negative or positive'''
num1 = 5 
if num1 > 0:
  print('Positive')
else:
  print('Negative')

'''print zero if input is given as zero'''
num2 = 0
if(num2 > 0):
  print('Positive')
else: 
  if num2 == 0:
    print('zero')
  else:
    print('Negative')

''' print even -1 as -1'''
num2 = 0
if(num2 > 0):
  print('Positive')
else: 
  if num2 == 0:
    print('zero')
  else:
    if num1 == -1:
      print(-1)
    else:
      print('negative')
# as you can see the code is complex to understand we go for elif 

'''2. elif :'''
num1=-1
if num1 > 0:
  print('positive')
elif num1 == 0:
  print('Zero')
elif num1 ==-1:
  print('-1')
elif num1 < 0:
  print('negative')
else:
  print('something')


'''2. LOOPS '''

'''3. JUMP STATEMENTS --- BREAK and CONTINUE '''
