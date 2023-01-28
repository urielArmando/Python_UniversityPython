value = int(input("Ingrese su calificación final\n>>"))

if 10 >= value >= 9:
    print("Calification: A")
elif 9 > value >= 8:
    print("Calification: B")
elif 8 > value >= 7:
    print("Calification: C")
elif 7 > value >= 6:
    print("Calification: D")
elif 6 > value >= 0:
    print("Calification: F")
else:
    print("Valor incorrecto (deben ser números del 0 al 10)")
