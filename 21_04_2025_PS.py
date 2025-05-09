

'''  2. Given a list of words, return a dictionary where the keys are words and values are their lengths.
 '''
# list1=['orange', 'banana', 'apple']

# res ={}
# for i in list1:
#   res[i] = len(i)

# print(res)  # {'orange': 6, 'banana': 6, 'apple': 5}

'''  4. Given two lists of equal length, create a dictionary where one list contains keys and the other contains values.
 '''
# list1=['orange', 'banana', 'apple']
# list2 = ['value1', 'value2', 'value3']

# res = {}

# for i in range(len(list1)):
#   res[list1[i]] = list2[i]

# print(res)  # {'orange': 'value1', 'banana': 'value2', 'apple': 'value3'}

'''  1. Given a list of numbers, count the occurrences of each number and return a dictionary.
 '''
# list1=[1,2,3,3,-2,6,7,6,2,7,2,2]

# frequencyDict = {}

# for i in list1:
#   if i in frequencyDict:
#     frequencyDict[i] += 1 # If the number i is already a key in freqDict, increase its value by 1
#   else:
#     frequencyDict[i] = 1  # If i is not present in freqDict, add it as a key with the initial value of 1

# print(frequencyDict)  # {1: 1, 2: 4, 3: 2, -2: 1, 6: 2, 7: 2}


''' 3. Given a string, return a dictionary where keys are characters and values are their occurrence.
 '''
# str1 = 'hippopotamus'

# frequencyDict = {}

# for i in str1:
#   if i in frequencyDict:
#     frequencyDict[i] += 1 
#   else:
#     frequencyDict[i] = 1  

# print(frequencyDict)  # {'h': 1, 'i': 1, 'p': 3, 'o': 2, 't': 1, 'a': 1, 'm': 1, 'u': 1, 's': 1}


''' 5. Swap keys and values of a dictionary. Store keys in a list. '''

# dict1 = {1: 'v1', 'k2':'v2', 'k1': 'v3', 'k4': 'v3'}
# res = {}

# for i, j in dict1.items():
#   res[j] = i

# print(res)   # {'v1': 1, 'v2': 'k2', 'v3': 'k4'}


'''level 2'''
# # now repeated values should get same keys a list of keys
# dict1 = {1: 'v1', 2: 'v1', 'k2':'v2', 'k1': 'v3', 'k4': 'v3'}
# res = {}

# for i, j in dict1.items():
#   if j not in res:
#     res[j] = [i]
#   else:
#     res[j].append(i)

# print(res)    # {'v1': [1, 2], 'v2': ['k2'], 'v3': ['k1', 'k4']}

''' 6. Given a dictionary, find the key with the highest value.
 '''
# dict1 = {'k1': 32, 'k2': -3, 'k3': 212, 'k4': 161}

# max_value = float('-inf')  # means in float max possible value 1.99999999999
# for i, j in dict1.items():
#   if j > max_value:
#     max_value = j
#     max_key = i

# print(max_value)  # 212
# print(max_key)    # k3
  
  

'''7. Given two dictionaries, merge them into one. If a key exists in both, sum their values.'''
# dict1 = {'1': 12, '2':3, '3': 4}
# dict2 = {'3': 5, '4': 5, '5': 2}

# res = {}
# for i, j in dict1.items():
#   res[i] = j
# print(res)

# for i, j in dict2.items():
#   if i in res:
#     res[i] = res[i] + j
#   else:
#     res[i] = j
  
# print(res)

'''8. Find if 2 strings are anagrams '''
# STOP POST TOPS
# AJAY JAYA
#  ELBOW BELOW

# 1st way to solve
# f_dict1 = {}
# f_dict2 = {}

# if f_dict1 == f_dict2:
#   print('Anagrams')

# 2nd way to solve

print(sorted('STOP') == sorted('TOPS'))  #True
print(sorted('STOP') == sorted('POTS'))  #True
print(sorted('STOP') == sorted('GAPS'))  #False





