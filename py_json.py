# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

userJSON = '{"first_name": "John", "last_name":"Doe", "age":30}'

# Parse to dict
user = json.loads(userJSON)
print(user)
print(user['first_name'])

car = {'Make': 'Ford', 'Model': 'Mustang', 'Year': 1937}

carJSON = json.dumps(car)
print(carJSON)