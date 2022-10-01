# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Joel'
age = 20

# print('Hello, my name is ' + name + ', and I am ' + str(age) + ' years old!')

# String Formatting

# Arguements by position
# print('My name is {name} and I am {age} years old!'.format(name = name, age = age))

# F-Strings
# print(f'Hello, my name is {name} and I am {age} years old!')

# String Methods
s = 'hello world'

# Capitalize
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lowercade
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
s = 'h'
print(s.count(s))

# Starts with
print(s.startswith('h'))

# Ends with
print(s.endswith('d'))

# Split
print(s.split())