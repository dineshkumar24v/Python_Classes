
'''Binary Search'''
# binary search will work based on sorted list only...if given a list 1st check whether sorted or not if not 1st do sorting and then do binary search....

# we can do binary serch only on the sorted list only
# so 1st check whethear a list is sorted or not

# list2 = [1,2,10,22,72,88,97,110]
# search_elem1 = 97

# def bin_search(list1, search_elem):
#   low =0
#   high=len(list1)-1

#   while low <= high:
#     mid = (low+high) // 2
#     if list1[mid] == search_elem:
#       return mid
#     elif list1[mid] > search_elem:
#       high = mid - 1
#     else:
#       low = mid + 1
  
#   return 'Not found'

# print(bin_search(list2, search_elem1))


''' Bubble Sort '''

# list1 = [21, -32, 45, -67, -3, -100]
# if i run this code for 6 times i get the sorted list:
# for i in range(len(list1)-1):
#   if list1[i] > list1[i+1]:
#     list1[i], list1[i+1] = list1[i+1], list1[i]

# print(list1)

# so instead of pasting it 6 times we can put that code in for loop and run it 6 times right...
list1 = [21, -32, 45, -67, -3, -100]
# so if we run the code 5 times we get the sorted list so here 5 means length of list-1

for j in range(0, len(list1)-1):
  for i in range(len(list1)-1 - j):
    if list1[i] > list1[i+1]:
      list1[i], list1[i+1] = list1[i+1], list1[i]

  print(list1)   # [-100, -67, -32, -3, 21, 45]


''' sort a string with more length at last '''
  # HINT: so earliar we compared values now we need to compare the length thats it

# list1 = ['21', '-32', '45', '-67', '-3', '-100']

# for j in range(0, len(list1)-1):
#   for i in range(len(list1)-1 - j):
#     if len(list1[i]) > len(list1[i+1]):
#       list1[i], list1[i+1] = list1[i+1], list1[i]

#   print(list1)  # ['21', '45', '-3', '-32', '-67', '-100']


  # so if we want descending order just change if len(list1[i]) < len(list1[i+1]): 
  



