



for cmp in range(1,11):
  for emp_id in range(1,31):
    if cmp ** 5 < 135 or emp_id < 15:
      break
    print(cmp, emp_id)
 


# pass ----
i=10
if i % 2 == 0:
  pass
else :
  print('nothing')



#ternary operator : one line code
age = 18
print('eligible to vote') if age > 18 else print('not eligible')

num=12
print('even') if num % 2 ==0 else print('odd')

