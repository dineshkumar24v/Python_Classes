#METHOD 3:
list1=[20,15, 26, 2, 98, 6]

# new_list = sorted(list1)
# print(list1)



''' Given array of N integer, the task is to replace each element of the array by its rank in the array
Input: [20, 15, 26, 2, 98, 6]
output: [4, 3, 5, 1, 6, 2] '''

# METHOD 4: DEEP COPY

# NOTE: to do a deep copy we need to import a module called copy--- so from the copy module iam importing the deepcopy function....
# list1 = [20, 15, 26, 2, 98, 6]
# import copy
# new_list = copy.deepcopy(list1)
# new_list.sort()
# print(new_list)
# print(list1) 

# output = [] 
# for i in list1:
#   # temp_res = new_list.index(i)
#   # print(temp_res+1)
# #   # or else one line code
#   output.append(new_list.index(i)+1)

# print(output)



list2 = [568, 89, 112, 88, 571]

def check_inc_order(input_num):
  temp = input_num 
  prev = 10
  while temp > 0:
    digit = temp % 10
    print(digit)
    if digit >= prev:
      return False
    prev = digit
    temp = temp // 10
  
  return True

for i in list1:
  print(check_inc_order(i))



''' find the lcm of 2 numbers: '''



''' find the GCD of a number '''