# Define list
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
# Print list nombres
print(nombres)
# Access to one element of list 'nombres'
print(nombres[0])
print(nombres[1])
# Accesses a list item 'nombres' backwards
print(nombres[-1])
print(nombres[-2])
# Print range of list
print(nombres[0:2])  # Don't include index 2
# Go to start of the list in index (not including it)
print(nombres[:3])
# from index to the end
print(nombres[1:])  # 1 to end of the list
# Change value of item in the list
nombres[3] = 'Ivone'
print(nombres)

for nombre in nombres:
    print(nombre)
else:
    print("Don't exist more names in the list")

# Length of the list
print(len(nombres))
# Add element to list 'nombres'
nombres.append('Lorenzo')
print(nombres)
# Insert element in index of the list
nombres.insert(1, 'Octavio')
print(nombres)
# Delete the latest item in the list
nombres.pop()
print(nombres)
# Delete item with index
del nombres[0]
print(nombres)

# Delete list
del nombres
