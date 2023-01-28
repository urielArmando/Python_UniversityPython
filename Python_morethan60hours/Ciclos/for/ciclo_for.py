'''
cadena = 'Hola'

for letra in cadena:
    print(letra)
else:
    print('Fin ciclo for')
'''

# Uso de break
'''
for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin ciclo for')
'''

# Use of continue
'''
for i in range(6): # range get number 0 to 6 (this is base to use understand continue)
    if i % 2 == 0:
        print(f'Valor: {i}')
'''

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')
