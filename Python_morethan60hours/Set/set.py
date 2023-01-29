# Define set
planets = {'Marte', 'Júpiter', 'Venus'}
print(planets)
# length of planets
print(len(planets))
# Find element in set
print('Marte' in planets)  # Returns boolean value
# Add more element in planets
planets.add('Tierra')
print(planets)
# Set don't support elements duplicate in set types
planets.add('Tierra')
print(planets)
# Delete element in set with possibility to trow error if it can't find
planets.remove('Tierra')
print(planets)
# Delete element in set, but no error if it can't find
planets.discard('Júpiter')
print(planets)
# Clear set
planets.clear()
print(planets)
# Delete set
del planets
