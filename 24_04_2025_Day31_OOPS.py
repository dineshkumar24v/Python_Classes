# OOPS: 
# 4 main pillars of OOPS 
# 1. Inheritance  2. Polymorphism  3. Encapsulation  4. Abstraction

# Inheritance: Child class inheritance from parent class 


class Calculator:
  def __init__(self, id1, manf_date1):
    self.id1 = id1
    self.manf_date1 = manf_date1
    print('Calculator constructor called')
  
  def add(self):
    print('Add function is called')

  def sub(self):
    print('Sub function is called')

class AdvCalculator(Calculator):
  def __init__(self, id1, manf_date1, price1):
    super().__init__(id1, manf_date1)
    self.price = price1
    print('Adv Claculator constructor called')
  
  def add(self):
    print('Add function from Advcalc is called')
  
  def sub(self):
    print('Sub of Adv Calc') 

class SuperCalculator(AdvCalculator):
  def __init__(self):
    print('Super constructor called')



  
adv1 = AdvCalculator('23', '01March', 3000)
sup1 = SuperCalculator()



''' Types of Inheritance : Single , multiLevel, multiple, hierarchial, Hybrid'''



# Eg: Multiple Inheritance:

class Lion:
  def roar(self):
    print('Lion is roaring')

  def hunt(self):
    print('Lion is hunting')

class Tiger:
  def hunt(self):
    print('Tiger is hunting')

class Liger(Lion, Tiger):  # MRO: Method Resolution Order
  pass

lg1 = Liger()
lg1.roar()
lg1.hunt()


''' PolyMorphism: Same entity acting in diferent forms in different situations'''

'''Method Over riding: '''
# if we write a function in child class which already exists in the parent class is called method over riding...

''' Method OverLoading: there is no method overloading concept in python '''
# but Overloading can be indirectly achieved through  arbitary and keyword arbitary *, **

'''Operator Overloading: '''
# Eg: print(2+3)
# Eg: print('2'+'3')

# print(2 & 3)
# print({1,2,3} & {2,3,4})

