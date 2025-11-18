''' How to append elements in a list to a new list'''

# list1 = [1, 2, 3, 82, -30, 44]

# new_list = []

# for i in list1:
#   # print(i)
#   new_list.append(i)

# print(new_list)

''' How to reverse an elements in a list'''

# METHOD 1:

# list1 = [1, 2, 3, 82, -30, 44]

# new_list = []
# for i in list1:
#   new_list.insert(0, i)

# list1 = new_list
# print(list1)


# METHOD 2 -- BY SWAPING METHOD
# list1 = [1, 2, 3, 82, -30, 44]

# low = 0
# high = len(list1) - 1

# while low < high:
#   # a, b = b , a   ---  swapping like this
#   list1[low], list1[high] = list1[high], list1[low]
#   low += 1
#   high -= 1

# print(list1)

''' How to reverse only the second half of the list'''
# list1 = [1, 2, 3, 82, -30, 44]

# low = len(list1) // 2
# high = len(list1) - 1

# while low < high:
#   # a, b = b , a   ---  swapping like this
#   list1[low], list1[high] = list1[high], list1[low]
#   low += 1
#   high -= 1

# print(list1)   # [1, 2, 3, 44, -30, 82]

''' How to reverse only the first half of the list'''
# list1 = [1, 2, 3, 82, -30, 44]

# low = 0
# high = len(list1) // 2 - 1

# while low < high:
#   # a, b = b , a   ---  swapping like this
#   list1[low], list1[high] = list1[high], list1[low]
#   low += 1
#   high -= 1

# print(list1)    # [3, 2, 1, 82, -30, 44]

'''find a given num in the list and print its index position '''
# list1 = [1, 2, 3, 82, -30, 44]
# find = 3

# flag = False
# for i in range(len(list1)):
#   if list1[i] == find:
#     flag = True
#     print('the position of',find, ' in list is', i)
#     break

# if flag == False:
#   print('Not found')

'''Write same in function'''

list1 = [1, 2, 3, 82, -30, 44]
find = -30

def linaer_search(input_list, find_elm):
  for i in range(len(input_list)):
    if list1[i] == find_elm:
      return i
    
  return 'Not found'

print(linaer_search(list1, find))