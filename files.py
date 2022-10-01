# Python has functions for creating, reading, updating, and deleting files.

# Create a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript.')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also love PHP.')
myFile.close()

# Read from a file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)