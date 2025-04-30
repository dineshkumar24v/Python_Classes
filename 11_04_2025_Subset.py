'''bubble sort :'''
# even trying to shorten the no of iterations for the earliars/ yesterdays code...
# i.e., optimizing the bubble sort method of yesterday...
# APPROACH : # this means that if even one element of the list is not sorted during 1st iteration means the list is already sorted only than y we need to do remaining itertions.... so that is the approach here

# list1 = [21, -32, 45, -67, -3, -100]

# for j in range(0, len(list1)-1):
#   flag = False
#   for i in range(len(list1)-1 - j):
#     if list1[i] > list1[i+1]:
#       flag=True
#       list1[i], list1[i+1] = list1[i+1], list1[i]
  
#   if flag == False: # this means that if even one element of the list is not sorted during 1st iteration means the list is already sorted so break the outer loop
#     break

#   print(list1)   # [-100, -67, -32, -3, 21, 45]



'''sort the lists in the list'''
'''Q: list1 = [[1,2], [-3, 4, 5], [22, 27], [-35]] output = [[-35], [-3, 4, 5], [1, 2], [22, 27]]'''
# HINT: just change here the list1[i][0] bec we need to check the list with in we have dfrnt lists

# list1 = [[1,2], [-3, 4, 5], [22, 27], [-35]] 

# for j in range(0, len(list1)-1):
#   flag = False
#   for i in range(len(list1)-1 - j):
#     if list1[i][0] > list1[i+1][0]:
#       flag=True
#       list1[i], list1[i+1] = list1[i+1], list1[i]
  
#   if flag == False: 
#     break

#   print(list1) 


''' Find the missing numbers Eg: input: 34571 -------> output: 26 missing'''
# HINT : 1st check for max digit and min digit of that number and check between numbers are there or not

# approach : 1st get every digits and append them to a list 
# [1, 7, 5, 4, 3] and then use the in-built function max(list1) => 7 and min(list1) => 1 to find the max and min digits of that number....

# num1 = 4559
# temp = num1
# dig_list1 = []

# while temp > 0:
#   digit = temp % 10
#   print(digit)
#   dig_list1.append(digit)
#   temp = temp // 10 # 3457

# print(dig_list1)

# max_elem, min_elem = max(dig_list1), min(dig_list1)

# for i in range(min_elem, max_elem + 1):
#   if i not in dig_list1:
#     print(i)  # 6 7 8


''' CONCEPT OF SUBSET '''
''' check if the array is subset of another array or not. If the arr2 contains elements which are there in arr1 then it is a subset of an array. 
arr1 = [1,3,4,5,2]
arr2 = [2,4,3,1,7,5,15]
output: arr1 is subset of arr2
'''
# my way:
# arr1 = [1,3,4,5,2]
# arr2 = [2,4,3,1,7,5,15]

# for i in arr1:
#   for j in arr2:
#     if i == j:
#       print(j, 'is the subset value of arr1')
      

# # class way:
# arr1 = [1,3,4,5,2]
# arr2 = [2,4,3,1,7,5,15]

# def check_subset(list1, list2):
#     for i in list1:
#       if i not in list2:
#          return "Not a subset"
      
#     return 'Subset'

# print(check_subset(arr1, arr2)) # subset


# set has an inbuilt function isSubset ----> so try by that method 


''' Find second largest element in a list (3rd later)'''

# list1= [20, 15, 26, 2, 98, 6]
# list1.sort()
# print(list1)  # [2, 6, 15, 20, 26, 98] sorted list...
# print(list1[-1]) # 98 we get largest...
# print(list1[-2]) # 26 we get second largest...


'''Method 1'''
list1 = [20, 15, 26, 2, 98, 6]
list1 = set(list1) # we are converting list to set so that list will have only unique elements i.e., no duplicates
# NOTE: set in unordered so 1st set the list and later sort the list...
list1 = list(list1)
list1.sort()
print(list1[-2])


'''Method 2: '''

max_elem = float('-inf')

for i in list1:
  if i > max_elem:
    max_elem = i

print(max_elem)

second_max = float('-inf')

for i in list1:
  if i > second_max and i != max_elem:
    second_max = i 