'''Time Complexity & Space Complexity'''
# code should be efficient i.e., should run the code in less time and should occupy the less space  
'''time --- means number of operations'''
# A code runs fast based on its number of operations
# Example :
# Method 1
# num = 25
# sum = 0
# for i in range(1, n+1): # it does 25 operations = it takes more time bec it has more number of operations
#   sum += i

# print(sum)

#METHOD 2:
# print((n*(n+1))//2)  # takes just 3 operations so it runs fast irrespective of the sysytem it runs

# n= 20 #40  #60
# for i in range(0, n):   #400  #1600  #3600
#   for j in range(0, n):
#     print("something")

'''time complexities of code:'''

#O(n square)

#O(n cube)

#O(1)  O(n) O(n square) O(n cube)

#log(n) < n
#O(log(n))
#O(nlog(n))

'''Order of Efficiency : = less time to ---> more time'''
# O(1) > O(logn) > O(n) >O(nlogn) > O(n square) > O(n cube)



'''Space Complexity / memory complexity -----> Additional memory'''

# O(1) - s.c ==> Although input increases the time you take to complete the code wont change

# sum = 0
# for i in range(1, n+1): #25
#   sum += i
# print(sum)

# LINEAR time Complexity Code --- O(n)
# s.c -- O(1)

# Method 2
# print((n*(n+1)//2))   # 3 or 1
#O(1)
#O(1)  - s.c

# list takes more space space complexcity increasing
# list1 = [1, 2, 3, 82, -30, 44]

# new_list = []
# for i in list1:
#   new_list.insert(0, i)

# list1 = new_list
# print(list1)


'''Q: I have a list1 = [245, 678, 901, 333] now i want the sum of the digits of each list item and also print the output of digits in list format only ouput = [11, 21, 10, 9]'''





