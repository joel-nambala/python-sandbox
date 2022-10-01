# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create a tuple
fruits = ('Apples', 'Mangoes', 'Grapes')
# print(fruits[1])

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set
fruits_set = {'Apples', 'Oranges', 'Mangoes'}
print(fruits_set)

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Remove fro set
fruits_set.remove('Grapes')

# Clear set
fruits_set.clear()

# Delete
del fruits_set
print(fruits_set)