matriz = []
usuario = int(input("escriba su numero: "))
matriz.append(usuario)
preg = input("Va a poner mas numeros? y para si, n para no")

while preg == "y" or preg == "Y":
    usuario = int(input("ponga otro numero "))
    matriz.append(usuario)
    preg = input("Va a poner mas numeros? y para si, otra tecla para no")

utte = list(reversed(matriz))

print (f"su lista invertida es {utte}")