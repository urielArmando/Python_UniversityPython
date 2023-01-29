tupla = (13, 1, 8, 3, 2, 5, 8)  # Define tuple
lista = []  # Creating variable type list avoid

for item in tupla:  # Iterate item in tuple
    if item < 5:  # Validate that item is smaller than 5
        lista.append(item)  # Adding item to list
print(lista)
