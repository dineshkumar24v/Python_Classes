''' NESTED LOOPS :'''




''' 10 companies and 30 employees '''

# for j in range(1, 11):
#   for i in range(1, 31):
#     print(j, i)


# # to print for only odd companies:
# for j in range(1, 11, 2):
#   for i in range(1, 31):
#      print(j, i)

# other way :
# for j in range(1, 11):
#    for i in range(1, 31):
#       if j%2==1 :
#          print(j, i)


# for j in range(1, 11):
#    for i in range(1, 31):
#       if j%2==1 and i>15:
#          print(j, i)
         

# for j in range(1, 11):
#    for i in range(1, 31):
#       if j%2==1 or i>15:
#          print(j, i)


# i=1
# for j in range(1, 11): 
#   while i<31:
#     print(j,i)
#     i+=1

# for j in range(1, 11):  # initial j value is 1
#   i=1
#   while i<31:
#     print(j,i)
#     i+=1

# j = 1
# while j<11: # initial j = 2
#   i=1
#   while i<31:
#     print(j,1)
#     i+=1
#   j+=1


# count = 0
# for j in range(1, 11):
#   for i in range(1, 31):
#     print(j,i)

# print(count)



'''JUMP STATEMENTS ---- 1.BREAK     2.CONTINUE'''
# in python we can use jump statements in only loops 

for i in range(1,10):
    print(i)
    if i==4:
        break 
    print(i)


for i in range(1,10):
    print(i)
    if i==4:
        print(i)
        break 


for i in range(1,10):
    print(i)
    if i==4:
        print(i)
        continue 


for i in range(1,10):
    print(i)
    if i==4:
        continue 
    print(i)

    





