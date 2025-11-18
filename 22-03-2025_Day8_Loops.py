'''Loops= loop means you come to the same condition again and again'''
'''For Loop'''
#advantages: decrease the code complexity, maintainability, decrease the code redundancy-repeating yourself,  increases code redability

'''Types of loop = for & while loops'''
'''for loop :'''
#  for loop we run it for the conditions we already know
#  we use for loop when i know the values
# In general we go for for loop when we know the values & use while loop when we know the condition

#FOR LOOP SYNTAX: two ways
# 1.
# for i in iterable:
list1=[1,24,3,4,5]  
for i in list1:   # we use this to get values
  print(i)  # 1 24 3 4 5

#2.
# for i in range(0,100)
for i in range(0,100):
  print(i)   # 0 to 99
  print(i+1)
  print(i+2)

# we use this to get indexes
for i in range(0, len(list1)):  # 0 to 4
  # print(i)  # 0 1 2 3 4   #
  print(list1[i])  # 1 24 3 4 5 # here we get items in list

'''print 1 to 20 Natural numbers using for loop'''
for i in range(0,21):
  print(i)  # 1 2 3 4 5 6 7 8 9 10 11 12 13 ......20

# second way:
num1 = 35
for i in range(1, num1+1):
  print(i)

'''print 1st 20 even numbers'''
for i in range(0,39,2):
  print(i)   # 0 2 4 6 8 10 12 14 16 18 20 .......38

# second way : print without using skip:
for i in range(0, 39):
  if i % 2 ==0:
    print(i)   # # 0 2 4 6 8 10 12 14 16 18 20 .......38

'''print odd numbers'''
for i in range(1,20,2):
  print(i)   # 1 3 5 7 9 11 13 15 17 19


'''sum of 1st n Natural Numbers:'''
sum = 0
for i in range(1, num1+1):
  sum += i  # sum = sum + i

print(sum)   # 630









''' WHILE LOOP '''

'''1. Print 1st 20 Natural Numbers'''
# num=1
# while num < 21:
#     print(num)
#     num+=1

'''Print 1st 20 EVEN Numbers'''
# num=2
# while num<40 :
#   print(num)
#   num+=2

'''Print 1st 20 ODD Numbers'''
# num=1
# while num<40 :
#   print(num)
#   num+=2

'''print table '''
# num=1
# while num<11 :
#   print(12, '*', num, '=', 12*num )
#   num+=1