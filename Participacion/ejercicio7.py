lista = []
usuario = int(input("escriba su numero: "))
lista.append(usuario)
preg = input("Va a poner mas numeros? y para si, n para no")

while preg == "y" or preg == "Y":
    usuario = int(input("ponga otro numero "))
    lista.append(usuario)
    preg = input("Va a poner mas numeros? s para si, otra tecla para no")

for i in lista:

    maximo = max(lista)
    minimo = min(lista)

print(f"La lista dada {lista}, su numero mayor es {maximo} y su numero menor es {minimo}")