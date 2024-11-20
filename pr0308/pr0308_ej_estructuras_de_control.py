"""
Crea en Python un programa que realice lo siguiente:
o Crea una lista de tuplas:
▪ (1,'a')
▪ (2,'b')
▪ (3,'c')
▪ (4,'d')
o Mostrar por pantalla el contenido de la lista
o Recorrer la lista con un bucle for y mostrar por pantalla cada elemento de la lista,
además de mostrar el primer elemento de la tupla y el segundo elemento de la
tupla
o Recorrer la lista con un bucle for y comprobar si el primer elemento de cada tupla
es un número par en ese caso postrar la segunda posición de la tupla, en caso
contrario mostrar la primera posición de la tupla
o Realiza lo mismo que en el punto anterior pero con un bucle while
"""

lista = [
    (1, 'a'),
    (2, 'b'),
    (3, 'c'),
    (4, 'd'),
]

print("MOSTRAR LA LISTA POR PANTALLA:")
print(lista)

print("\nRECORRIDO CON UN BUCLE FOR:")
for tupla in lista:
    print(f"{tupla}, {tupla[0]}, {tupla[1]}")

print("\nRECORRIDO CON BUCLE FOR PAR E IMPAR:")
for tupla in lista:
    if tupla[0] % 2 == 0:
        print(tupla[1])
    else:
        print(tupla[0])

print("\nRECORRIDO CON UN BUCLE WHILE PAR E IMPAR:")
contador = 0
while len(lista)>contador:
    tupla = lista[contador]
    if tupla[0] % 2 == 0:
        print(tupla[1])
    else:
        print(tupla[0])
    contador += 1