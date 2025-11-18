'''Week 1: Topics - Conditional statements, For and while (At max 2 days)'''
'''1. If else and if else ladder 
a. Easy Questions:'''


'''1. Write a program to check if a given number is positive, negative, or zero'''

# number = float(input("Enter a number : "))
# if number > 0 :
#     print("given number is positive")
# elif number == 0 :
#     print("given number is zero")
# else:
#     print("given number is negative")

'''2. Determine if a number is odd or even.'''


# num = int(input("Enter a number : "))
# if num == 0 :
#     print("given number is zero")
# elif num % 2 == 0 :
#     print("given number is even")
# else:
#     print("given number is odd")

'''3. Check if a person is eligible to vote (age >= 18).'''

# age = float(input("Enter your age : "))
# if age >= 18 :
#     print("you are eligible")  
# else:
#     print("not eligible")

# print("you are eligible") if age >=18 else print("not eligible")

''' 4. Write a program to find the greatest of two numbers.'''

# num1 = float(input("Enter a number for num1 : "))
# num2 = float(input("Enter a number for num2 : "))
# print('num1 is greatest') if num1 > num2 else print('both are equal') if num1 == num2 else print ('num2 is greater')

''' 5. Print "Pass" if a student scores more than 40 marks;
otherwise, print "Fail."'''

# marks = int(input("marks obtaine : "))
# print("pass") if marks > 40 else print("fail")  


'''6. Write a program to display the day of the week based on a number input (1 for Monday , 2 for Tuesday etc...) '''
# num=int(input('enter a number '))
# if num==1:
#   print('Monday')
# elif num==2:
#   print('Tuesday')
# elif num==3:
#   print('Wednesday')
# elif num==4:
#   print('Thursday')
# elif num==5:
#   print('Friday')
# elif num==6:
#   print('Saturday')
# elif num==7:
#   print('Sunday')
# else:
#   print('invalid number')  


'''7. Implement a Simple Calculator'''
# num1=float(input('enter num1 '))
# num2=float(input('enter num2 '))
# op=input('enter operator ')
# if op in['+','add','a'] :
#   print(num1+num2)
# elif op in['-','sub','s'] :
#   print(num1-num2)
# elif op in['*','mul','m'] :
#   print(num1*num2)
# elif op in['/','div','d'] :
#   if num2 != 0:
#     print(num1/num2)
#   else :
#     print('Division by zero is not possible')  
# else :
#   print('Invalid Operator')    


'''8. Write a program to display the name of a month based on
the month number (1 for January, 2 for February, etc.).
'''

month = int(input("Enter a number for month : "))

if month == 1 :
    print('January')
elif month == 2 :
    print('February')
elif month == 3 :
    print('March')
elif month == 4 :
    print('April')
elif month == 5 :
    print('May')
elif month == 6 :
    print('June')
elif month == 7 :
    print('July')
elif month == 8 :
    print('August')
elif month == 9 :
    print('September')
elif month == 10 :
    print('October')
elif month == 11 :
    print('November')
elif month == 12 :
    print('December')
else:
    print('invalid month')

''' ---------------------------------------b. MEDIUM QUESTIONS: -------------------------------------'''

''' ----------- 1. Write a program to find the greatest of the three Numbers? --------- '''
# num1=int(input('enter num1 '))
# num2=int(input('enter num2 '))
# num3=int(input('enter num3 '))
# if num1>num2 and num1>num3 :
#   print(num1, ' is greatest')
# elif num2>num1 and num2>num3 :
#   print(num2, ' is greatest')
# else :
#   print(num3, ' is greatest')    

'''or optimised code'''
# num1=int(input('enter num1 '))
# num2=int(input('enter num2 '))
# num3=int(input('enter num3 '))
# if num2 > num3 :
#   print(num1, ' is greatest')
# elif num2>num1 and num2>num3 :
#   print(num2, ' is greatest')
# else :
#   print(num3, ' is greatest')    


''' ----------- 2. Check if a year is a leap year? -------------'''
'''if century = should divide by 400    and if non-century = shhould divide by 4'''
# year = 1796
# if year % 400 == 0:   # checking century
#   print()
# elif year % 100 != 0 and year % 4 ==0:    # checking non-century
#   print('leap year')
# else:
#   print('not a leap year')


# year=int(input('enter any year '))
# if (year%4==0 and year%100 != 0) or year%400==0 :    
#   print(year, ' is a leap year')
# else :
#   print(year, ' is not a leap year')  
  


'''----------- 3. Write a program to classify a character entered by the user as a vowel , consonant, or neither?----------'''
# alphabet=input("Enter a single Character :").lower()
# if len(alphabet)!=1:
#     print("Invalid")
# else:
#     if alphabet in['a','e','i','o','u']:
#         print("Vowels")
#     elif alphabet.isalpha():
#         print("consonant")
#     else:
#         print("Special characters")


'''-------- 4. Calculate the grade of a student based on the ,arks they score:---------'''

# marks=int(input('enter marks '))
# if marks>=90 and marks<=100 :
#   print('Grade A')
# elif marks>=80 and marks<=89 :
#   print('Grade B')
# elif marks>=70 and marks<=79 :
#   print('Grade A')
# elif marks>0 and marks<=70 :
#   print('Fail')
# else:
#   print('invalid input, enter marks from 0 to 100')


'''-------- 5. Write a program to check if three sides length form a valid triangle? ----------'''

side1=float(input('enter side 1 of a traiangle '))
side2=float(input('enter side 2 of a traiangle '))
side3=float(input('enter side 3 of a traiangle '))

if side1+side2>side3 and side2+side3>side1 and side1+side3>side2 :
  print('forms a valid triangle')
else :
  print('cannot form a valid triangle')  


'''--------- Buzz & fizzBuzz-------------------'''
num=int(input('enter any number '))
## 
if num%15==0 :
  print('fizzBuzz')
elif num%5==0 :
  print('buzz')
elif num%3==0 :
  print('fizz')
else :
  print('Invalid Number') 