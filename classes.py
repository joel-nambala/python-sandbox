# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create a class
class User:
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    
  def greeting(self):
    return f'My name is {self.name} and I am {self.age}!'
  
  def has_birthday(self):
    self.age += 1
    
# Extend a class
class Customer(User):
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0
    
  def set_balance(self, balance):
    self.balance = balance
    
  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}!'
  
# Init an object
joel = User('Joel Nambala', 'joel@gmail.com', 22)

# Init a customer
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())

joel.has_birthday()
print(joel.greeting())