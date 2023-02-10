import random

def lista(n):
    lista = [4] * n
    for i in range (n):
        lista[i] = random.randint(1,100000)
    return lista

n= int(input("copie cuantos numeros quiere"))

lista = lista(n)
print (lista)