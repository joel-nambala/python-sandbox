# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create a dictionary
person = {
  'first_name': 'Joel',
  'last_name' : 'Nambala',
  'age' : 30
}

# Get a value
# print(person['first_name'])
# print(person.get('last_name'))

# Add key/value
person['phone'] = '0792555952'

# Get the keys
# print(person.keys())

# Get the items
# print(person.items())

# Copy a dict
person2 = person.copy()
person2['city'] = 'Nairobi'

# Remove item
del(person2['age'])
person2.pop('phone')

# Clear
person.clear()

# Get the length
print(len(person2))

people = [
  {'name': 'Joel', 'age': 50},
  {'name': 'Kevin', 'age': 45},
  {'name': 'Jessica', 'age': 20},
  {'name': 'Mike', 'age': 33}
]
print(people)