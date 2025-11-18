# SET = set is a collection of finite unique elements
# set is hetrogeneous, which has unique elements(i.e., duplication is not allowed ) and it is unordered(i.e., it dont print set values as given which is why INDEXING is not possible in set)

s1={1,2,3,4,5,6,7,8,9}
print(type(s1))    # <class 'set'>
print(s1)   # {1, 2, 3, 4, 5, 6, 7, 8, 9}  

# no duplications are allowed
s1={1,2,3,4,5,6,7,8,9,1,2,3,4}
print(s1)    # {1, 2, 3, 4, 5, 6, 7, 8, 9}  





#  dictionaries --- it is a collection of key value pairs and is mutable also 


#  
dict1 = {1:'harish', 2:'suresh', 3:'Ganesh', 4:'prakash'}
print(dict1)
print(dict1[2])     # suresh

db_values = {'db_name': 'localhost/3000', 'db_pass':'secret', 'timeout':30}


# Why String in Python is immutable?
# id ing
str1=5
print(id(str1))   # 140727504865848
str2=5
print(id(str2))   # 140727504865848


str3 = 'suresh'
print(id(str3))    # 1499841976944
str4 = 'suresh'
print(id(str4))    # 1499841976944


str1='12.5'
# print(int(str1))  
print(float(str1))  # 12.5


# Type Conversion  ##################
# float ----------- to ----------- int
num1 = 4.5
print(int(num1))    # 4
print(num1)         # 4.5

# int ----to ------float
num1 = int(num1)
num1 = float(num1)
print(num1)         # 0


# string ---------- to ---------list
str1= 'string example'





