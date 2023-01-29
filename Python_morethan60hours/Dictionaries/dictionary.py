# Dictionary ( key and value)
dictionary = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(dictionary)
# Length dictionary
print(len(dictionary))
# Accessing element in dictionary
print(dictionary['IDE'])
# Other form:
print(dictionary.get('OOP'))
# Modifying element in dictionary
dictionary['IDE'] = 'integrated development environment'
print(dictionary)
# Travers dictionary
for key, value in dictionary.items():  # Get key and value of dictionary
    print(key, value)

for term in dictionary.keys():  # Get only keys of dictionary
    print(term)

for value in dictionary.values():  # Get only values of dictionary
    print(value)

# Validate if one element exist in dictionary
print('IDE' in dictionary)  # Returns boolean value
# Add element to dictionary
dictionary['PK'] = 'Primary Key'
print(dictionary)
# Remove element
dictionary.pop('DBMS')  # Args is a key in dictionary
# Cleaning dictionary
dictionary.clear()
print(dictionary)
# Delete dictionary
del dictionary
