# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1,2,3,4,5))
# print(numbers, numbers2)

# Get a value
print(fruits[1])

# Get the length of a list
print(len(fruits))

# Append to the list
fruits.append('Mangoes')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)