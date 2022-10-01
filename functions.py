# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create a function
def sayHello(name = 'Joel'):
  print(f'Hello {name}')
  
# Return values
# def getSum(num1, num2):
#   return num1 + num2

# num = getSum(3, 5)
# print(num)

def cutFruits(fruit):
  return fruit * 4

def fruitProcessor(apples, oranges):
  applePieces = cutFruits(apples)
  orangePieces = cutFruits(oranges)
  
  juice = f'Juice made with {applePieces} pieces of apple and {orangePieces} pieces of orange.'
  print(juice)

fruitProcessor(3, 5)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
print(getSum(10, 3))