''' OOPS in Python'''
#Class: A class is a collection of objects. Classes are created by keyword class. Attributes are the variables that belong to a class.
# Object : An Object is an instance of a Class.
# Self Parameter: self parameter is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.
#Constructor:
# function is called a Method inside class...

# __init__ Method :  __init__ method is the constructor in Python, automatically called when a new object is created. It initializes the attributes of the class.

# if we remove self we get error = TypeError: Calculator.add() takes 0 positional arguments but 1 was given
# this keyword represent the current object in JS similarly in Python we have self 
# if we write a functions inside a class than we call it as a method not a function..

# constructor--> it is a special type of method which runs every time you create a new object...if you create
# constructor also has a def keyword likewiswe function syntax: def __name__():

# to chech how many variables does an object have we have a function called vars
class Calculator:   # Blueprint or definition
  def __name__(self,id,color,manf_date):  # this is a constructor and its calls automatically
    self.id=id
    self.color=color
    self.manf_date=manf_date

  def add():   # here self is passed as an argument automatically
    print('this is an add function')

  def mul():
    print('this is a function for multiplication')

calc1 = Calculator('1','black','01Feb')
calc2 = Calculator('2','red','02Feb')
calc1.exp_date='feb2026'  # manual passing an extra 


calc1.add()
calc2.mul()


# constructor --- is also a method
'''Types of variable : -- 2 types:
 1. Instance Variable   2. Class/Static variable'''
''' 1. Instance Varaible --- Object is nothing but an instance of a variable 
here the variable depends on the object'''

# Eg: car1.color = 'blue'

''' 2. Class/Static Variable : here the variable doesnot depends on an object'''

# Eg: company_name: CASIO


# NOTE: an instance variables can be accessed by using an instance
# NOTE: class/static variable can be accessed by using an instance or a class
# NOTE: we cannot access an instance variables using a class
# NOTE: class variables can be accessed via the class name or an object...
# NOTE: Instance variables are accessed via the object 





''' 3 types of methods: 1. Class Method 2. Static Method  3. Instance Method'''
# Instance method--- should have atleast one instance...
# class method & static variable are definitly should use a decorator


