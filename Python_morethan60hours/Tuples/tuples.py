# Tuple is immutable
# Define tuple
fruits = ('Naranja', 'Platano', 'Guayaba')  # This can't be modified
# To define one element in tuple: e.g fruits = ('Naranja',) coma is required
print(fruits)
# Length of fruits
print(len(fruits))
# Accessing one element
print(fruits[0])
# Navigation inverse
print(fruits[-1])
# Print items by range
print(fruits[0:2])
# Traverse tuple
for fruit in fruits:
    print(fruit, end=' / ')
# Change values in fruits tuple
fruitsList = list(fruits)  # Convert tuple in type list
fruitsList[0] = 'Pera'
fruits = tuple(fruitsList)  # Convert list in tuple. Changing value index 0 to 'Pera' in new tuple
print('\n', fruits)
# Delete tuple
del fruits
