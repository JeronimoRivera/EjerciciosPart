import random

def matriz (fila, columna):

    M = []
    for i in range(fila):
        lista = []
        for j in range(columna):
            lista.append(random.randint(0,100))

        M.append(lista)

    return (M)

fila = int(input("Cuantas filas desea: "))
columna = int(input("Cuantas columnas desea: "))

M = matriz(fila, columna)

print (M)
